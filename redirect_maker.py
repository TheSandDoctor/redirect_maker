#!/usr/bin/env python3.6
import configparser, json, mwclient
from time import sleep
from mwclient import errors


def save_wrap(res):
    site,title = res
    page = site.Pages[title]
    print(str(page.page_title))
    #if not page.exists: ##NOT IN USE##
         #save_edit(page, site, "#REDIRECT [[User:RhinosF1]]")
    else:
        input("EXISTS " + str(page.page_title))
        if 'Y':
           save_edit(page, site, "#REDIRECT [[
        else:
           print('Change Refused')


def save_edit(page, site, text)
    edit_summary = """Create userspace redirect. (BOT)"""
    time = 0
    while True:
        if time > 1:
            break
        try:
            page.save(text, summary=edit_summary, bot=False, minor=True)
        except errors.ProtectedPageError:
            print('Could not edit ' + page.page_title + ' due to protection')
            time += 1
        except errors.EditError:
            print("Error")
            time += 1
            sleep(5)  # sleep for 5 seconds before trying again
            continue
        break


def gen_page_titles(month, month_dict, year):
    return "User:RhinosF1/Archives_" + str(year) + "/" + str(month) + "_" + "(" + month_dict.get(month) + ")"


def main():
    site = mwclient.Site(('https', 'en.wikipedia.org'), '/w/')
    config = configparser.RawConfigParser()
    config.read('credentials.txt')
    try:
        site.login(config.get('enwiki_sandbot', 'username'), config.get('enwiki_sandbot', 'password'))
    except errors.LoginError as e:
        print(e)
        raise ValueError("Login failed.")

    month_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    # since ranges are not inclusive, end must always be +1 above
    lst = [gen_page_titles(month, month_dict, year) for year in range(2018, 2019) for month in range(1, 13)]
    for i in map(save_wrap, [(site, x) for x in lst]):
        pass

if __name__ == "__main__":
    main()
