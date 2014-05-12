import atomac as at
from time import sleep

def verify(statement):
    if statement:
        print 'passed'
    else:
        print 'failed'

#defs
bundleId = 'com.kapralos.Unbelievable'
appTitle = 'Unbelievable'
upperCaseRadioTitle = 'Upper case'
lowerCaseRadioTitle = 'Lower case'
transformButtonTitle = 'Transform text'

at.launchAppByBundleId(bundleId)
app = at.getAppRefByBundleId(bundleId)

# there is no notification app finish launch notification in atomac, so set a 1-sec sleep
sleep(1)
appWindow = app.windows()[0]
print 'App title: ' + appWindow.AXTitle

print appWindow.findAll()

inputTextLabel = appWindow.findFirst(AXRole='AXStaticText')
print inputTextLabel

inputTextField = appWindow.findFirst(AXRole='AXTextField')
prefixCheckBox = appWindow.findFirst(AXRole='AXCheckBox')
upperCaseRadio = appWindow.findFirst(AXRole='AXRadioGroup').findFirst(AXTitle=upperCaseRadioTitle)
lowerCaseRadio = appWindow.findFirst(AXRole='AXRadioGroup').findFirst(AXTitle=lowerCaseRadioTitle)
transformButton = appWindow.findFirst(AXRole='AXButton', AXTitle=transformButtonTitle)
resultTextView = appWindow.findFirst(AXRole='AXScrollArea').findFirst(AXRole='AXTextArea')

inputTextField.AXValue = 'text1'
transformButton.Press()
verify(resultTextView.AXValue == 'PREFIXTEXT1')

inputTextField.AXValue = 'text2'
prefixCheckBox.Press()
transformButton.Press()
verify(resultTextView.AXValue == 'TEXT2')

inputTextField.AXValue = 'tEXt3'
prefixCheckBox.Press()
lowerCaseRadio.Press()
transformButton.Press()
verify(resultTextView.AXValue == 'prefixtext3')

inputTextField.AXValue = 'tEXt4'
prefixCheckBox.Press()
transformButton.Press()
verify(resultTextView.AXValue == 'text4')

menu = app.AXMenuBar
undoButton = menu.findFirst(AXRole='AXMenuBarItem', AXTitle='Edit').AXChildren[0].findFirst(AXTitle='Undo')
undoButton.Press()
verify(inputTextField.AXValue == 'tEXt3')

selectAllButton = menu.findFirst(AXRole='AXMenuBarItem', AXTitle='Edit').AXChildren[0].findFirst(AXTitle='Select All')
deleteButton = menu.findFirst(AXRole='AXMenuBarItem', AXTitle='Edit').AXChildren[0].findFirst(AXTitle='Delete')
selectAllButton.Press()
deleteButton.Press()
verify(inputTextField.AXValue == '')

aboutButton = menu.findFirst(AXRole='AXMenuBarItem', AXTitle=appWindow.AXTitle).AXChildren[0].findFirst(AXTitle='About ' + appWindow.AXTitle)
aboutButton.Press()