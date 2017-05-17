import neovim
import urllib2


@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('ImprovizSend')
    def improvizSend(self, args):
        text = "\n".join(self.vim.current.buffer[:])
        self.vim.out_write("Sending to Improviz\n")
        try:
            url = "http://%s:%s/read" % (
                self.vim.vars['improviz_host'],
                self.vim.vars['improviz_port']
            )
            resp = urllib2.urlopen(url, text)
            self.vim.out_write("%s\n" % resp.read())
        except urllib2.URLError, e:
            self.vim.err_write("URL Error: %s\n" % str(e.reason))
        except urllib2.HTTPError, e:
            self.vim.err_write("HTTP Error: %s\n" % str(e.code))

    @neovim.function('ImprovizToggleText')
    def improvizToggleTxt(self, args):
        self.vim.out_write("Sending to Improviz\n")
        try:
            url = "http://%s:%s/toggle/text" % (
                self.vim.vars['improviz_host'],
                self.vim.vars['improviz_port']
            )
            resp = urllib2.urlopen(url, data="")
            self.vim.out_write("%s\n" % resp.read())
        except urllib2.URLError, e:
            self.vim.err_write("URL Error: %s - %s\n" % (str(e.reason), url))
        except urllib2.HTTPError, e:
            self.vim.err_write("HTTP Error: %s\n" % str(e.code))
