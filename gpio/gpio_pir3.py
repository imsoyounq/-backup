from gpiozero import MotionSensor
'''
class MotionSensor(SmoothedInputDevice):
    def __init__(self, pin=15, queue_len=1, sample_rate=10, threshold=1, partial=False):
        super(MotionSensor, self).__init__(pin. pull_up=False, threshold=threshold, queue_len=queue_len, sample_wait=1 / sample_rate, partial=partial)
        try:
            self._queue.start()
        except:
            self.close()
            raise
'''
pir = MotionSensor(15)
pir.wait_for_motion()
print "Motion detected!"

