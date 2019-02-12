from busquedas import *
from formularios import *
from logins import *
from selecciones import *
from clics import *
from vaciar import *
import HtmlTestRunner


class google(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com/')
        self.driver.fullscreen_window()

        self.busq = objeto_busquedas(self.driver)
        self.form = objeto_formularios(self.driver)
        self.selec = objeto_selecciones(self.driver)
        self.log = objeto_logins(self.driver)
        self.clic = objeto_clics(self.driver)
        self.vaciar = objeto_vaciar(self.driver)

        self.driver.implicitly_wait(1)

    def test_busqueda_plink(self):
        self.busq.busqueda_por_name('q', 'selenium en python')
        self.clic.clic_por_partial_link_text('selenium · PyPI')
        time.sleep(2)

    def test_buscar_imagenes(self):
        self.busq.busqueda_por_name('q', 'selenium en java')
        self.clic.clic_por_link_text('Imágenes')
        time.sleep(2)

    def test_busqueda_en_link(self):
        self.form.formulario_name(1,'sseelleenniiuumm','','','','','q','','','','')
        time.sleep(1.5)
        self.vaciar.limpiar_campo_name('q')
        self.busq.busqueda_por_name('q', 'selenium')
        self.clic.clic_por_link_text('Videos')
        self.clic.clic_por_partial_link_text('¿Qué es Selenium? - 1 Minuto - YouTube')

    def test_python_descarga(self):
        self.busq.busqueda_por_name('q', 'python')
        self.clic.clic_por_partial_link_text('Welcome to Python.org')
        self.clic.clic_por_xpath('//*[@id="downloads"]/a')
        self.clic.clic_por_xpath('//*[@id="touchnav-wrapper"]/header/div/div[2]/div/div[2]/p/a')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='mi_reporte'))
