import qi
import argparse
import functools
import time
from datetime import datetime
import threading
from script import steps
import random

class Robin(object):

    def __init__(self, app):
        super(Robin, self).__init__()

        app.start()
        session = app.session

        self.current_step = 0

        # Default wait time
        self.speech_wait_time = 2  
        self.is_waiting_speech = False      

        # Retrieve the required services
        self.ALAutonomousLife = session.service("ALAutonomousLife")
        self.ALRobotPosture = session.service("ALRobotPosture")
        self.ALMotion = session.service("ALMotion")
        self.ALTextToSpeech = session.service("ALTextToSpeech")
        self.ALMemory = session.service("ALMemory")
        self.ALSpeechRecognition = session.service("ALSpeechRecognition")
        self.ALBehaviorManager = session.service("ALBehaviorManager")
        self.ALLeds = session.service("ALLeds")

        # Disable autonomous life
        self.ALAutonomousLife.setState('disabled')
        self.ALMotion.setBreathEnabled('Head', True)
        self.blink_timer = threading.Timer(random.randint(3,8), self.doBlink)
        self.blink_timer.start()

        # Put the robot in the seated position, with stiffness released so that it doesn't overheat
        self.ALRobotPosture.goToPosture('Crouch', 0.5)
        names = ['RKneePitch', 'LKneePitch', 'RAnklePitch', 'LAnklePitch', 'RAnkleRoll', 'LAnkleRoll']
        self.ALMotion.setStiffnesses(names, 0.0)

        # Language, volume, and speech tempo
        self.ALTextToSpeech.setLanguage('Dutch')
        self.ALTextToSpeech.setVolume(0.8)
        self.ALTextToSpeech.setParameter('speed', 85.0)
        self.ALSpeechRecognition.pause(True)
        self.ALSpeechRecognition.setLanguage('Dutch')

        # For speech detection/recognition
        self.speechactivity = self.ALMemory.subscriber("SpeechDetected")
        self.speech_id = self.speechactivity.signal.connect(functools.partial(self.onSpeech, "SpeechDetected"))        

        self.word_detected = self.ALMemory.subscriber("WordRecognized")
        self.word_detected_id = self.word_detected.signal.connect(functools.partial(self.onWord, "WordRecognized")) 

        self.speech_timer = threading.Timer(self.speech_wait_time, self.silenceComplete)
       
        # Wait for head sensor to be touched to start the interaction
        self.processNextStep()

    def processNextStep(self):
    	if (steps[self.current_step]['type'] == 'head'):
            self.touch = self.ALMemory.subscriber("TouchChanged")
            self.sensor_id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

        elif (steps[self.current_step]['type'] == 'timed'):
            time.sleep(steps[self.current_step]['timing'])
            self.ALTextToSpeech.say(steps[self.current_step]['text'])

            self.determineNextStep()
            self.processNextStep()

        elif (steps[self.current_step]['type'] == 'silence'):
            self.speech_wait_time = steps[self.current_step]['silence_time']
            # self.is_waiting_speech = True
            self.ALSpeechRecognition.removeAllContext()
            self.ALSpeechRecognition.setVocabulary(['asdf'], False)
            time.sleep(0.25)
            self.ALSpeechRecognition.pause(False)
            try:
                self.ALSpeechRecognition.unsubscribe('Robin')
            except:
                pass
            self.ALSpeechRecognition.subscribe('Robin')

            # print "test"

        elif (steps[self.current_step]['type'] == 'boolean'):
            self.ALSpeechRecognition.removeAllContext()
            self.ALSpeechRecognition.setVocabulary(['ja', 'ok', 'nee'], True)
            time.sleep(0.25)
            self.ALSpeechRecognition.pause(False)
            try:
                self.ALSpeechRecognition.unsubscribe('Robin')
            except:
                pass
            self.ALSpeechRecognition.subscribe('Robin')


        elif (steps[self.current_step]['type'] == 'breathe'):
            self.breathingExercise()
            self.determineNextStep()
            self.processNextStep()

    def determineNextStep(self):
        if ('next' in steps[self.current_step]):
            self.current_step = steps[self.current_step]['next']
        else:
            self.current_step += 1

    def onTouched(self, strVarName, value):
        # Disconnect to the event when talking,
        # to avoid repetitions
        self.touch.signal.disconnect(self.sensor_id)

        self.determineNextStep()
        self.processNextStep()

    def silenceComplete(self):
    	self.is_waiting_speech = False
        try:
            self.ALSpeechRecognition.unsubscribe('Robin')
        except:
            pass

        self.ALSpeechRecognition.pause(True)
        print "Person did not speak for a while!"
        self.ALTextToSpeech.say(steps[self.current_step]['text'])    	
        self.determineNextStep()
        self.processNextStep()

    def onSpeech(self, eventName, value):
    	print "Speech detected!"
    	print value

        if (steps[self.current_step]['type'] == 'silence'):    	
            if value == 1:
                self.is_waiting_speech = True
    	    	# self.first_speech = True
                self.speech_timer.cancel()

            if value == 0 and self.is_waiting_speech:# and self.first_speech == True:
                self.speech_timer.cancel()
                self.speech_timer = threading.Timer(self.speech_wait_time, self.silenceComplete)
                self.speech_timer.start()      

    def onWord(self, eventName, value):
        print "Word detected!"
        print value[0]

        if (steps[self.current_step]['type'] == 'boolean'):
            if ('ja' in value[0] or 'ok' in value[0]):
                try:
                    self.ALSpeechRecognition.unsubscribe('Robin')
                except:
                    pass

                self.ALSpeechRecognition.pause(True)        		
                self.current_step = steps[self.current_step]['positive']
                self.processNextStep()
            elif ('nee' in value[0]):
                try:
                    self.ALSpeechRecognition.unsubscribe('Robin')
                except:
                    pass

                self.ALSpeechRecognition.pause(True)
                self.current_step = steps[self.current_step]['negative']
                self.processNextStep()

    def doBlink(self):
        self.ALLeds.off('FaceLeds')
        time.sleep(0.25)
        self.ALLeds.on('FaceLeds')
        self.blink_timer = threading.Timer(random.randint(3,8), self.doBlink)
        self.blink_timer.start()

    def breathingExercise(self):
    	for i in range(5):
            # Choregraphe bezier export in Python.
            names = list()
            times = list()
            keys = list()

            names.append("LElbowRoll")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[-1.05382, [3, -0.0133333, 0], [3, 0.653333, 0]], [-1.07376, [3, -0.653333, 0], [3, 1, 0]], [-1.07376, [3, -1, 0], [3, 0.666667, 0]], [-1.20875, [3, -0.666667, 0], [3, 1.66667, 0]], [-1.20875, [3, -1.66667, 0], [3, 0, 0]]])

            names.append("LElbowYaw")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[-0.779314, [3, -0.0133333, 0], [3, 0.653333, 0]], [-1.38985, [3, -0.653333, 0], [3, 1, 0]], [-1.38985, [3, -1, 0], [3, 0.666667, 0]], [-0.49399, [3, -0.666667, 0], [3, 1.66667, 0]], [-0.49399, [3, -1.66667, 0], [3, 0, 0]]])

            names.append("LHand")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[0.0116, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.0116, [3, -0.653333, 0], [3, 1, 0]], [0.0116, [3, -1, 0], [3, 0.666667, 0]], [0.0116, [3, -0.666667, 0], [3, 1.66667, 0]], [0.0116, [3, -1.66667, 0], [3, 0, 0]]])

            names.append("LShoulderPitch")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[1.42198, [3, -0.0133333, 0], [3, 0.653333, 0]], [-0.0644701, [3, -0.653333, 0], [3, 1, 0]], [-0.0644701, [3, -1, 0], [3, 0.666667, 0]], [0.868202, [3, -0.666667, 0], [3, 1.66667, 0]], [0.868202, [3, -1.66667, 0], [3, 0, 0]]])

            names.append("LShoulderRoll")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[0.154892, [3, -0.0133333, 0], [3, 0.653333, 0]], [1.04768, [3, -0.653333, 0], [3, 1, 0]], [1.04768, [3, -1, 0], [3, 0.666667, 0]], [0.25, [3, -0.666667, 0], [3, 1.66667, 0]], [0.25, [3, -1.66667, 0], [3, 0, 0]]])

            names.append("LWristYaw")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[0.148756, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.00455999, [3, -0.653333, 0], [3, 1, 0]], [0.00455999, [3, -1, 0], [3, 0.666667, 0]], [0.736278, [3, -0.666667, 0], [3, 1.66667, 0]], [0.736278, [3, -1.66667, 0], [3, 0, 0]]])

            names.append("RElbowRoll")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[1.05083, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.983336, [3, -0.653333, 0], [3, 1, 0]], [0.983336, [3, -1, 0], [3, 0.666667, 0]], [1.17202, [3, -0.666667, 0], [3, 1.66667, 0]], [1.17202, [3, -1.66667, 0], [3, 0, 0]]])

            names.append("RElbowYaw")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[0.782298, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.546062, [3, -0.653333, 0], [3, 1, 0]], [0.546062, [3, -1, 0], [3, 0.666667, 0]], [0.213184, [3, -0.666667, 0], [3, 1.66667, 0]], [0.213184, [3, -1.66667, 0], [3, 0, 0]]])

            names.append("RHand")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[0.0132, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.0132, [3, -0.653333, 0], [3, 1, 0]], [0.0132, [3, -1, 0], [3, 0.666667, 0]], [0.0132, [3, -0.666667, 0], [3, 1.66667, 0]], [0.0132, [3, -1.66667, 0], [3, 0, 0]]])

            names.append("RShoulderPitch")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[1.44354, [3, -0.0133333, 0], [3, 0.653333, 0]], [-0.670316, [3, -0.653333, 0], [3, 1, 0]], [-0.670316, [3, -1, 0], [3, 0.666667, 0]], [0.7471, [3, -0.666667, 0], [3, 1.66667, 0]], [0.7471, [3, -1.66667, 0], [3, 0, 0]]])

            names.append("RShoulderRoll")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[-0.151908, [3, -0.0133333, 0], [3, 0.653333, 0]], [-1.12446, [3, -0.653333, 0], [3, 1, 0]], [-1.12446, [3, -1, 0], [3, 0.666667, 0]], [-0.30991, [3, -0.666667, 0], [3, 1.66667, 0]], [-0.30991, [3, -1.66667, 0], [3, 0, 0]]])

            names.append("RWristYaw")
            times.append([0, 1.96, 4.96, 6.96, 11.96])
            keys.append([[-0.139636, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.136484, [3, -0.653333, 0], [3, 1, 0]], [0.136484, [3, -1, 0], [3, 0.666667, 0]], [-0.529272, [3, -0.666667, 0], [3, 1.66667, 0]], [-0.529272, [3, -1.66667, 0], [3, 0, 0]]])

            breathing_speech_timer = threading.Timer(0.1, self.breathingSpeech)
            breathing_speech_timer.start()

            try:
                self.ALMotion.angleInterpolationBezier(names, times, keys)
            except BaseException, err:
                print err

        self.ALRobotPosture.goToPosture('Crouch', 0.5)
        names = ['RKneePitch', 'LKneePitch', 'RAnklePitch', 'LAnklePitch', 'RAnkleRoll', 'LAnkleRoll']
        self.ALMotion.setStiffnesses(names, 0.0)
        self.ALMotion.setBreathEnabled('Head', True)


    def breathingSpeech(self):
    	time.sleep(1)
        self.ALTextToSpeech.say('Adem in.')
        time.sleep(3)
        self.ALTextToSpeech.say('Adem uit.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["ReactToTouch", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    robin = Robin(app)
    app.run()