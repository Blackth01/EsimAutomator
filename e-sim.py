#coding utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import strftime, gmtime
import time
import os

x = 1
path = os.getcwd()

navegar = webdriver.Firefox(executable_path=r"%s/geckodriver" % path)

def trabalho (usuario, senha, server):
    global x
    while(True):
            navegar.get('https://%s.e-sim.org' % server)
            
            username = navegar.find_element_by_id('registeredPlayerLogin')
            username.send_keys(usuario)

            password = navegar.find_element_by_name('password')
            password.send_keys(senha)

            Logar = navegar.find_element_by_xpath("//button[@value='Login']")
            Logar.click()
            try:
                navegar.get('https://%s.e-sim.org/work.html' % server)
            except:
                navegar.get('https://%s.e-sim.org/work.html' % server)

            done = False
            while(done == False):
                try:
                    Trabalhar = navegar.find_element_by_id('workButton')
                    Trabalhar.click()
                except:
                    done = True
                

            navegar.get('https://%s.e-sim.org/train.html' % server)
            done = False
            while (done == False):
                try:
                    Treinar = navegar.find_element_by_id('trainButton')
                    Treinar.click()
                except:
                    done = True

            try:
                notifications = navegar.find_element_by_xpath("//li[@id='numero1']/a[@class='blank-icon']")
                print ("Voce nao possui notificacoes no servidor %s" % server)
            except:
                try:
                   notifications = navegar.find_element_by_xpath("//li[@id='numero1']/a[@class='active-icon']")
                   notifications.click()
                   time.sleep(5)
                   tempo = time.strftime("%Y_%A_%b_%d_%H:%M", gmtime())
                   navegar.save_screenshot("%s_screenshotNoti-%s.png" % (server, tempo))
                   print ("Voce possui notificacoes no servidor %s, verifique os screenshots" % server)
                except:
                    x-= 1
                    print ("Ocorreu um erro no servidor %s, reiniciando as tarefas..." % server)
                    break
            try:
                messages = navegar.find_element_by_xpath("//li[@id='numero2']/a[@class='blank-icon']")
                print ("Voce nao possui mensagens no servidor %s" % server)
            except:
                messages = navegar.find_element_by_xpath("//li[@id='numero2']/a[@class='active-icon']")
                messages.click()
                time.sleep(5)
                tempo = time.strftime("%Y_%A_%b_%d_%H:%M", gmtime())
                navegar.save_screenshot("%s_screenshotMsg-%s.png" % (server, tempo))
                print ("Voce possui mensagens no servidor %s, verifique os screenshots" % server)

            try:
                confirmar = navegar.find_element_by_id('taskButtonWork')
                print ("Nao foi possivel trabalhar no servidor %s" % server)
            except:
                print ("Tarefas concluidas com sucesso no servidor %s" % server)
            break

while (x < 5):
    if (x == 1):
        trabalho("username", "password", "secura")
    if (x == 2):
        trabalho("username", "password", "primera")
    if (x == 3):
        trabalho("username", "password", "suna")
    if (x == 4):
        trabalho("username", "password", "alpha")
    x += 1
navegar.quit()

