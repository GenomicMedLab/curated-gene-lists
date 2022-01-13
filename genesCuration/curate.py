import pandas as pd
import pdb
import openpyxl
import html
import sys
import datetime

def main():

    data = pd.read_excel('cancer_genes_with_pcgp_210921.xlsx',sheet_name='final',index_col=0)

    # check args
    try:
        if sys.argv[1] == 'pcgp':
            filterField = 'PCGP category (PMID 26580448)'
            directory = 'byPCGP'
            panelBuckets = getPCGP(data)

        elif sys.argv[1] == 'mardis':
            filterField = 'Preferred list (Mardis)'
            directory = 'byMardis'
            panelBuckets = getMardis(data)

        elif sys.argv[1] == 'cgc':
            filterField = 'CGC list'
            directory = 'byCGC'
            panelBuckets = getCGC(data)

        elif sys.argv[1] == 'panel':
            filterField = 'Panel'
            directory = 'byPanel'
            panelBuckets = getPanels(data)

        else:
            print('Invalid argument')
            print('Defaulting to PCGP')
            filterField = 'PCGP category (PMID 26580448)'
            panelBuckets = getPCGP(data)
    except:
        panelBuckets = getPCGP(data)

    # Write individual buckets out to file for debugging purposes
    df3 = pd.DataFrame()
    df3 = df3.assign(buckets=panelBuckets)
    writer = pd.ExcelWriter('buckets.xlsx')
    df3.to_excel(writer,sheet_name='buckets')
    writer.save()

    # For each individual case, just set the bucket ID as if it ignored the comma split? Probably the quickest way to fix
    for i in panelBuckets:
        fix = fixThePanel(i)
        writeTSV(data,fix,filterField,directory)

def fixThePanel(bucket):

    # From excel file, some buckets are messing up due to extra commas. This is a hard coded fix (hopefully a fix)
    if bucket == 'CGC Genetics USA OncoRisk Expanded (NGS panel for 89 genes' or bucket == 'including CNV analysis)':
        fixedBucket = 'CGC Genetics USA OncoRisk Expanded (NGS panel for 89 genes, including CNV analysis)'
    elif bucket == 'Phosphorous' or bucket == 'Inc. Brain and Nervous System Cancer Panel':
        fixedBucket = 'Phosphorous, Inc. Brain and Nervous System Cancer Panel'

    elif bucket == 'CGC Genetics USA OncoRisk (NGS panel for 48 genes':
        fixedBucket = 'CGC Genetics USA OncoRIsk (NGS panel for 48 genes, including CNV analysis)'

    elif bucket == 'and PNS Cancer: Deletion/Duplication Panel':
        fixedBucket = 'EGL Genetics Brain, CNS, and PNS Cancer: Deletion/Duplication Panel'
    elif bucket == 'and PNS Cancer Panel: Sequencing and CNV Analysis':
        fixedBucket = 'EGL Genetics Brain, CNS, and PNS Cancer Panel: Sequencing and CNV Analysis'

    elif bucket == 'Mayo Clinic Laboratories Neuro-Oncology Expanded Gene Panel with Rearrangement':
        fixedBucket = 'Mayo Clinic Laboratories Neuro-Oncology Expanded Gene Panel with Rearrangement Tumor'

    else:
        fixedBucket = bucket

    return(fixedBucket)

def getPanels(df):

    crosscheck = list()

    for i in df['Panel']:

        if type(i)==float:
            print('FLOAT')
            pass
        else:
            temp = i.split(', ')
            for j in temp:
                if j in crosscheck:
                    print('Already there')
                else:
                    crosscheck.append(j)

    return(crosscheck)

def getCGC(df):

    # Do the same thing as getPanels, but for the CGC List

    crosscheck = list()

    for i in df['CGC list']:

        if type(i)==float:
            print('FLOAT')
            pass
        else:
            temp = i.split(', ')
            for j in temp:
                if j in crosscheck:
                    print('Already there')
                else:
                    crosscheck.append(j)

    return(crosscheck)

def getPCGP(df):
   # Do the same thing as getPanels, but for the PCGP List

    crosscheck = list()

    for i in df['PCGP category (PMID 26580448)']:

        if type(i)==float:
            print('FLOAT')
            pass
        else:
            temp = i.split(';')
            for j in temp:
                if j in crosscheck:
                    print('Already there')
                else:
                    crosscheck.append(j)

    return(crosscheck)

def getMardis(df):

    # Do the same thing as getPanels, but for the Mardis Preferred List

    crosscheck = list()

    for i in df['Preferred list (Mardis)']:

        if type(i)==float:
            print('FLOAT')
            pass
        else:
            temp = i.split(', ')
            for j in temp:
                if j in crosscheck:
                    print('Already there')
                else:
                    crosscheck.append(j)

    return(crosscheck)

def writeTSV(df,bucket,filter_field,directory):

    # Write function for saving split results. Change filename or whatever accordingly

    filename = bucket.replace('/',' ')
    filename = filename.replace('(',' ')

    if bucket == 'EGL Genetics Brain' or bucket == 'CNS' or bucket == 'Tumor' or bucket == '':
        return

    try:
        df2 = df[df[filter_field].str.contains(bucket)==True]
    except:
        print('Something went wrong sorting by bucket')
        pdb.set_trace()

    # Initialize excel file
    try:
        writer = pd.ExcelWriter(directory + '/' + filename + '.xlsx')
    except:
        print('Something went wrong with filename')
        pdb.set_trace()

    # Write each results to a separate sheet (probably more efficient way to do this)
    df2.to_excel(writer,sheet_name='genes')

    writer.save()


if __name__ == '__main__':
    main()

# Make DF's by like PMID?
# Make DF's by like gene panel?
#    this would be a ' if panel exists, do thing'
# Make DF's by curated source?
#    this is what the message says to do, split up into TSVs by curated source
#





###################### REFERENCE CODE FOR ACCESSING DATA ########################
#
#   data['Panel'].value_counts() # Panels that each individual gene is on
#
#
#
#
