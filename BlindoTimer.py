from threading import Timer


class RepeatedTimer(object):
    def __init__(self, interval):
        self._timer     = None
        self.interval   = interval/1000 # change second? into millisecond
        self.function = None
        self.args = None
        self.kwargs = None
        self.is_running = False
        #self.start()

    def _run(self):
        self.is_running = False
        #self.start()
        self.function(*self.args, **self.kwargs)
        self.stop()
        self._timer = None

    def start(self, function, *args, **kwargs ):
        if not self.is_running:
            self.function = function
            self.args = args
            self.kwargs = kwargs
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False