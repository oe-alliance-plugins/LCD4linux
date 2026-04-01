from setuptools import setup
import setup_translate

pkg = 'Extensions.LCD4linux'
setup(name='enigma2-plugin-extensions-lcd4linux',
       version='3.0',
       description='Web/DPF/Samsung LCD Ansteuerung',
       package_dir={pkg: 'LCD4linux'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'plugin.png', 'History.txt', 'data/Clock1/*.png', 'data/Clock10/*.png', 'data/Clock2/*.png', 'data/Clock3/*.png', 'data/Clock4/*.png', 'data/Clock5/*.png', 'data/Clock6/*.png', 'data/Clock7/*.png', 'data/Clock8/*.png', 'data/Clock9/*.png', 'data/*.png', 'data/skin_data.xml', 'data/default.lcd', 'data/default.colorlcd220', 'data/default.colorlcd400', 'data/default.vuduo2', 'data/default.colorlcd720', 'data/default.colorlcd480', 'data/default.bwlcd255', 'data/default.colorlcd800', 'data/audio/*.png', 'meteo/*.png', 'meteo/meteo-template.html', 'wetter/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
