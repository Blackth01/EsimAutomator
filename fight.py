#coding: utf-8
from selenium import webdriver
from time import sleep
import os

path = os.getcwd()

browser = webdriver.Firefox(executable_path=r"%s/geckodriver" % path)

def setup (choice, side):
    while(True):
            raw_input('Choose the battle, set your food, gift and weapon preferences on game and press enter')

            if(side == 'B'):
                fight = browser.find_element_by_id("fightButtonBerserk2")
            else:
                fight = browser.find_element_by_id("fightButtonBerserk1")

            food = browser.find_element_by_id("eatButton2")
            gift = browser.find_element_by_id("useGiftButton2")


            if(choice == 'G'):
                giftlimit = int(input('How many gift limits do you want to fight?'))
                fighting(browser, giftlimit, gift, fight)
            else:
                foodlimit = int(input('How many food limits do you want to fight?'))
                giftlimit = 0
                if(choice == 'B'):
                    giftlimit = int(input('How many gift limits do you want to fight?'))
                fighting(browser, foodlimit, food, fight)
                if(giftlimit):
                    fighting(browser, giftlimit, gift, fight)
            break

def fighting(browser, limit, button1, button2):
    i=0
    while(i < limit):
        try:
            button1.click()
            button1.click()
            button2.click()
            button2.click()
            i+=2
            print('fought 2x')
        except:
            sleep(0.5)
            blockmodals = browser.find_elements_by_class_name("pico-close")
            try:
                for modal in reversed(blockmodals):
                    modal.click()
            except:
                sleep(0.5)
                blockmodals = browser.find_elements_by_class_name("pico-close")
                for modal in reversed(blockmodals):
                    modal.click()


choice = raw_input('Fight (G)ifts, (F)oods or (B)oth? Default F: ')
side = raw_input('Choose the side (A or B) Default A: ')

setup(choice, side)

