from os import stat, symlink
from os.path import isfile
from Components.Renderer.Renderer import Renderer
from enigma import ePixmap, eTimer
try:
	from enigma import eMediaDatabase  # noqa: F401
	DPKG = True
except ImportError:
	DPKG = False


class PixmapLcd4linux(Renderer):
	def __init__(self):
		Renderer.__init__(self)
		self.mTime = 0
		self.swap = False
		self.L4Ltimer = eTimer()
		if DPKG:
			self.L4Ltimer_conn = self.L4Ltimer.timeout.connect(self.changed)
		else:
			self.L4Ltimer.callback.append(self.changed)

	GUI_WIDGET = ePixmap

	def postWidgetCreate(self, instance):
		self.changed((self.CHANGED_DEFAULT,))

	def changed(*s):
		sel = s[0]
		sel.L4Ltimer.stop()
		if isfile("/tmp/l4ldisplay.png"):
			try:
				mtime = stat("/tmp/l4ldisplay.png").st_mtime
				if sel.mTime != mtime:
					if sel.instance:
						if sel.swap:
							if not isfile("/tmp/l4ldisplaycp.png"):
								symlink("/tmp/l4ldisplay.png", "/tmp/l4ldisplaycp.png")
							sel.instance.setPixmapFromFile("/tmp/l4ldisplaycp.png")
						else:
							sel.instance.setPixmapFromFile("/tmp/l4ldisplay.png")
						sel.mTime = mtime
						sel.swap = not sel.swap
					else:
						sel.mTime = 0
			except Exception:
				pass
			sel.L4Ltimer.start(200, True)
