
        def precmd(self, line):
            print('Preparing to execute: {}'.format(line))
            return cmd.Cmd.precmd(self, line)

        def postcmd(self, stop, line):
            print('Finished executing: {}'.format(line))
            return cmd.Cmd.postcmd(self, stop, line)
