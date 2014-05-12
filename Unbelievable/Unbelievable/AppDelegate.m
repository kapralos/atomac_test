//
//  AppDelegate.m
//  Unbelievable
//
//  Created by Evgeniy Kapralov on 12/05/14.
//  Copyright (c) 2014 Evgeniy Kapralov. All rights reserved.
//

#import "AppDelegate.h"

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
    [self.inputTextField setStringValue:@"ololo"];
    [self.prefixCheckBox setState:NSOffState];
    self.upperCaseRadio.state = NSOnState;
    self.lowerCaseRadio.state = NSOnState;
}

- (void)selectTransformButton:(id)sender
{
    [self.resultTextView setString:@"ololo"];
}

@end
