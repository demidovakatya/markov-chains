class Logger:
    def error(self, text):
        print("ERROR: " + text)

    def info(self, text):
        print("INFO: " + text)

    def warn(self, text):
        print("WARNING: " + text)

    def log(self, text):
        print(text)

    def log(self, level, text):
        if level == 'error':
            self.error(self, text)
        elif level == 'info':
            self.info(self, text)
        elif level == 'warn':
            self.info(self, text)
        else:
            self.log(self, text)
