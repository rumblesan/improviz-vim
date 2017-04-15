import neovim
import urllib2


@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('ImprovizSend')
    def doItPython(self, args):
        text = "\n".join(self.vim.current.buffer[:])
        try:
            resp = urllib2.urlopen("http://localhost:3000/read", text)
            self.vim.command("echo '%s'" % resp.read())
        except urllib2.URLError, e:
            self.vim.command("echo 'URL Error': %s" % str(e.reason))
        except urllib2.HTTPError, e:
            self.vim.command("echo 'HTTP Error': %s" % str(e.code))
