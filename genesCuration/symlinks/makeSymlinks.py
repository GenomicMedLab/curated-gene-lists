import os
import pandas as pd
import pdb

def main():

    with open('genePanels.yaml') as f:
        disease_folders = f.read().splitlines()

    for i in disease_folders:
        panels = getPanels(i)
        panels_miller, panels_pauk, panels_paau = splitPanels(panels)
        makeSyms(panels_miller,panels_pauk,panels_paau,i)

    pass

def strReplace(st):
    st = st.replace(' ','\ ')
    st = st.replace('(','\(')
    st = st.replace(')','\)')
    return(st)

def splitPanels(panels_list):

    panelCounter = 0
    miller_list = list()
    pauk_list = list()
    paau_list = list()

    for i in panels_list:

        # Miller List
        if panelCounter == 0:
            if i == 'PANEL APP UK':
                panelCounter = 1
            else:
                i = strReplace(i)
                miller_list.append(i)

        # Panel App UK
        elif panelCounter == 1:
            if i == 'PANEL APP AU':
                panelCounter = 2
            else:
                i = strReplace(i)
                pauk_list.append(i)

        # Panel App AU
        elif panelCounter == 2:
            try:
                i = strReplace(i)
                paau_list.append(i)
            except:
                pass
        else:
            pass

    return(miller_list,pauk_list,paau_list)

def getPanels(disease_class):
    with open('panels/' + disease_class + '.yaml') as f:
        panels_list = f.read().splitlines()

    return(panels_list)

def makeSyms(panels_miller,panels_pauk,panels_paau,disease_class):

    try:
        os.system('mkdir ../../diseases/' + disease_class)
    except:
        pass

    for i in panels_miller:
        try:
            os.system('ln -s ../../data/miller/byPanel/' + i + ' ' + '../../diseases/' + disease_class + '/' + i)
        except:
            pass

    for i in panels_pauk:
        try:
            os.system('ln -s ../../data/panelapp/uk/' + i + ' ' + '../../diseases/' + disease_class + '/' + i)
        except:
            pass

    for i in panels_paau:
        try:
            os.system('ln -s ../../data/panelapp/au/' + i + ' ' + '../../diseases/' + disease_class + '/' + i)
        except:
            pass

if __name__ == '__main__':
    main()