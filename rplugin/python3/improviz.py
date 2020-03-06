import neovim
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    def makeErrLine(self, buf, err):
        name = buf.name
        line = err['line']
        col = err['column']
        msg = err['message'].strip()
        errline = "\"%s:%d:%d: %s\"" % (name, line, col, msg)
        self.vim.out_write(errline)
        return errline

    def addErrsToLocationList(self, errs):
        cmd = "lexpr [%s]" % ", ".join(errs)
        self.vim.out_write(cmd)
        self.vim.command(cmd)

    @neovim.function('ImprovizSend')
    def improvizSend(self, args):
        buf = self.vim.current.buffer
        code = buf[:]
        text = str.encode("\n".join(code))
        self.vim.out_write("Sending to Improviz\n")
        self.vim.command("lexpr []")  # clear the location list
        try:
            url = "http://%s:%s/read" % (
                self.vim.vars['improviz_host'],
                self.vim.vars['improviz_port']
            )
            resp = urlopen(url, text)
            data = json.loads(resp.read())
            if data['status'] == 'ok':
                self.vim.out_write("%d lines sent OK\n" % len(code))
            else:
                errs = []
                for e in data['payload']:
                    errs.append(self.makeErrLine(buf, e))
                self.addErrsToLocationList(errs)
                self.vim.err_write("%d errors found\n" % len(errs))
        except URLError as e:
            self.vim.err_write("URL Error: %s\n" % str(e.reason))
        except HTTPError as e:
            self.vim.err_write("HTTP Error: %s\n" % str(e.code))

    @neovim.function('ImprovizToggleText')
    def improvizToggleText(self, args):
        self.vim.out_write("Sending to Improviz\n")
        try:
            url = "http://%s:%s/toggle/text" % (
                self.vim.vars['improviz_host'],
                self.vim.vars['improviz_port']
            )
            resp = urlopen(url, data=str.encode(""))
            self.vim.out_write("%s\n" % resp.read())
        except URLError as e:
            self.vim.err_write("URL Error: %s - %s\n" % (str(e.reason), url))
        except HTTPError as e:
            self.vim.err_write("HTTP Error: %s\n" % str(e.code))

    @neovim.function('ImprovizNudgeBeat')
    def improvizNudgeBeat(self, args):
        if args[0]:
            t = str(args[0])
        else:
            t = "0.25"
        self.vim.out_write("Nudging Beat %s\n".format(t))
        try:
            url = "http://%s:%s/nudge/%s" % (
                self.vim.vars['improviz_host'],
                self.vim.vars['improviz_port'],
                t
            )
            resp = urlopen(url, data=str.encode(""))
            self.vim.out_write("%s\n" % resp.read())
        except URLError as e:
            self.vim.err_write("URL Error: %s - %s\n" % (str(e.reason), url))
        except HTTPError as e:
            self.vim.err_write("HTTP Error: %s\n" % str(e.code))

    @neovim.command('ImprovizSend')
    def improvizSendCommand(self):
        self.improvizSend([])

    @neovim.command('ImprovizNudgeBeat', nargs=1)
    def improvizNudgeBeatCommand(self, args):
        self.improvizNudgeBeat(args[0])

    @neovim.command('ImprovizToggleText')
    def improvizToggleTextCommand(self):
        self.improvizToggleText([])
