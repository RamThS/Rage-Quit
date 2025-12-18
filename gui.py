import wx
import Game

class StartPage(wx.Frame):
    def __init__(self, parent=None, title="Rage Quit"):
        super(StartPage, self).__init__(parent, title=title, size=(600, 400))

        # Panel
        panel = wx.Panel(self)
        panel.SetBackgroundColour("grey")

        # Layout
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Title
        title_text = wx.StaticText(panel, label="Rage Quit", style=wx.ALIGN_CENTER)
        title_font = wx.Font(28, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_text.SetFont(title_font)
        title_text.SetForegroundColour("cyan")
        vbox.Add(title_text, flag=wx.ALIGN_CENTER | wx.TOP, border=40)

        # Play button
        play_btn = wx.Button(panel, label="▶ Play", size=(200, 50))
        play_btn.SetBackgroundColour("green")
        play_btn.SetForegroundColour("white")
        play_btn.Bind(wx.EVT_BUTTON, self.on_play)
        vbox.Add(play_btn, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        # Exit button
        exit_btn = wx.Button(panel, label="✖ Exit", size=(200, 50))
        exit_btn.SetBackgroundColour("red")
        exit_btn.SetForegroundColour("white")
        exit_btn.Bind(wx.EVT_BUTTON, self.on_exit)
        vbox.Add(exit_btn, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        # Apply layout
        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    # Button actions
    def on_play(self, event):
        self.Hide()
        Game.run_game()
        self.Close()

    def on_exit(self, event):
        self.Close()

# Run the app
if __name__ == "__main__":
    app = wx.App(False)
    frame = StartPage()
    app.MainLoop()