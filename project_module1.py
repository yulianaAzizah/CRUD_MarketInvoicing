invoice = [
    {
        'Invoice Number'    : 'ICL001',
        'Date'              : '20/01/2022',
        'Customer'          : 'Nael Siregar',
        'Item'              : 'Canvas Shoes',
        'Status'            : 'Close'
    },
    {
        'Invoice Number'    : 'ICL002',
        'Date'              : '14/02/2022',
        'Customer'          : 'Rifat Dzaka',
        'Item'              : 'Cardigan',
        'Status'            : 'Open'
    }
]

def mainMenu () :
    while(True) :
        menu = input('''
            ========================== QUCIKINVOICE.ID ==========================

            1. Invoice List
            2. Create New Invoice
            3. Invoice Payment Status Update
            4. Completed Payment
            5. Exit
            Pick a Number :  ''')
        if (menu == '1') :
            searchInvoice ()
        elif (menu == '2') :
            createInvoice ()
        elif (menu == '3') :
            updateInvoice () 
        elif (menu == '4') :
            deleteInvoice ()
        elif (menu == '5') :
            print('                      \tTHANKYOU VERY MUCH !')
            break
        else :
            print('                      \tINVALID INPUT !')

# MENU FOR READ DATA
def searchInvoice () :
    while(True) :
        invoiceList = input('''
            ========================== Invoice List ==========================
            1. All Invoice List
            2. Search Invoice 
            3. Back to Main Menu 
            Choose Menu : ''')
        if (invoiceList == '1') : 
            if invoice != [] :
                print('Invoice Number\t|Date    \t|Customer\t|Item\t        |Status')
                for i in range (len(invoice)) :
                    print('{}       \t|{}\t|{}\t|{}\t|{}'.format(invoice[i]['Invoice Number'], invoice[i]['Date'],invoice[i]['Customer'], invoice[i]['Item'],invoice[i]['Status']))
            elif invoice == [] :
                print('Invoice Not Found')
        elif (invoiceList == '2') :
            if invoice == [] :
                print('                      \tInvoice Not Found')
            elif invoice != [] :
                invNumber = input('Invoice Number : ').upper()
                for i in range (len(invoice)) :
                    if invNumber == invoice [i]['Invoice Number'] :
                        print('Invoice Number\t|Date    \t|Customer\t|Item\t        |Status')
                        print('{}       \t|{}\t|{}\t|{}\t|{}'.format(invoice[i]['Invoice Number'], invoice[i]['Date'],invoice[i]['Customer'], invoice[i]['Item'],invoice[i]['Status']))
                        break
                else :
                    print('                      \tInvoice Not Found')
        elif (invoiceList == '3') :
            break

# MENU FOR CREATE DATA
def createInvoice () :
    while(True) :
        invoiceList = input('''
                ========================== Create New Invoice ==========================
                1. Add Invoice Data
                2. Back to Main Menu
                Choose Menu : ''')
        if (invoiceList == '1') :
            invNumber = input('Invoice Number (ICLXXX): ').upper()
            for i in range(len(invoice)) :
                if invNumber == invoice [i]['Invoice Number'] :
                    print('                      \tInvoice Already Exist')
                    break
                else : 
                    invDate = input('Invoice Date (DD/MM/YYYY) : ')
                    custName = input('Customer : ')
                    itemName = input('Item Name : ')
                    invStatus = input('Invoice Status (Open/Close) : ')
                    confirmation = input('Do you want to save the data? (Y/N) : ').upper()
                    if (confirmation == 'Y') :
                        invoice.append({
                        'Invoice Number'    : invNumber,
                        'Date'              : invDate,
                        'Customer'          : custName,
                        'Item'              : itemName,
                        'Status'            : invStatus
                        })
                        print('                      \tData has been saved')
                        break
                    elif(confirmation == 'N') :
                        break
                    else :
                        print('                      \tInvalid Input, Please Re-Input')
        elif(invoiceList == '2'):
            break

# MENU FOR UPDATE DATA
def updateInvoice () :
    while(True) :
        invoiceList = input('''
                ========================== Invoice Payment Status Update ==========================
                1. Update Invoice Payment Status
                2. Back to Main Menu
                Choose Menu : ''')
        if (invoiceList == '1') :
            invNumber = input('Invoice Number : ').upper()
            for i in range (len(invoice)) :
                if invNumber == invoice [i]['Invoice Number'] :
                    print('Invoice Number\t|Date    \t|Customer\t|Item\t        |Status')
                    print('{}       \t|{}\t|{}\t|{}\t|{}'.format(invoice[i]['Invoice Number'], invoice[i]['Date'],invoice[i]['Customer'], invoice[i]['Item'],invoice[i]['Status']))
                    confirmation = input('Do you want to update this data? (Y/N) : ').upper()
                    if (confirmation == 'Y') :
                        newValue = input('Payment Status Update : ')
                        confirmation2 = input('Are you sure want to update this Payment Status? (Y/N) : ').upper()
                        if (confirmation2 == 'Y') :
                            invoice [i]['Status'] = newValue
                            print('                      \tInvoice Payment Status Updated')
                            break
                        elif(confirmation2 == 'N') :
                            break
                    elif(confirmation == 'N') :
                        break
            else :
                print('         \tInvoice Not Found')
        elif (invoiceList == '2') :
            break

# MENU FOR DELETE DATA
def deleteInvoice() :
    while(True) :
        invoiceList = input('''
                ========================== Delete Invoice ==========================
                1. Delete Invoice Data
                2. Back to Main Menu
                Choose Menu : ''')
        if (invoiceList == '1') :
            invNumber = input('Invoice Number : ').upper()
            for i in range(len(invoice)) :
                if invNumber == invoice[i]['Invoice Number'] :
                    confirmation = input('Do you want to delete this Invoice? (Y/N) : ').upper()
                    if (confirmation == 'Y') :
                        del invoice[i]
                        print('                      \tInvoice Deleted')
                        break
                    elif(confirmation == 'N') :
                        break
            else :
                print('                      \tInvoice Not Found')
        elif (invoiceList == '2') :
            break

mainMenu()