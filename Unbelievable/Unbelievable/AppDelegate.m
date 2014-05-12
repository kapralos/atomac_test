//
//  AppDelegate.m
//  Unbelievable
//
//  Created by Evgeniy Kapralov on 12/05/14.
//  Copyright (c) 2014 Evgeniy Kapralov. All rights reserved.
//

#import "AppDelegate.h"

#define TEXT_PREFIX @"prefix"

@interface AppDelegate()

@property (weak) IBOutlet NSTextField* inputTextField;
@property (weak) IBOutlet NSButton* prefixCheckBox;
@property (weak) IBOutlet NSButtonCell* upperCaseRadio;
@property (weak) IBOutlet NSButtonCell* lowerCaseRadio;
@property IBOutlet NSTextView* resultTextView;

- (IBAction)selectTransformButton:(id)sender;

@end

@implementation AppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    // Insert code here to initialize your application
}

- (void)selectTransformButton:(id)sender
{
    NSString* result = (self.prefixCheckBox.state == NSOnState) ? [NSString stringWithFormat:@"%@%@", TEXT_PREFIX, self.inputTextField.stringValue] : self.inputTextField.stringValue;
    if (self.upperCaseRadio.state == NSOnState)
    {
        result = [result uppercaseString];
    }
    else
    {
        result = [result lowercaseString];
    }
    self.resultTextView.string = result;
}

@end
