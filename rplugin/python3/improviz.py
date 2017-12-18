import neovim
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('ImprovizSend')
    def improvizSend(self, args):
        text = str.encode("\n".join(self.vim.current.buffer[:]))
        self.vim.out_write("Sending to Improviz\n")
        try:
            url = "http://%s:%s/read" % (
                self.vim.vars['improviz_host'],
                self.vim.vars['improviz_port']
            )
            resp = urlopen(url, text)
            self.vim.out_write("%s\n" % resp.read())
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
