#include <Clipboard.h>
#include <Application.h>
#include <Message.h>

#include <stdio.h>

main(){
    const char *text;
    int32 textLen;
    BApplication app("application/x-vnd.jrabbit.RandomCrap");
    BMessage *clip = (BMessage *)NULL;
    if (be_clipboard->Lock()) {
        if ((clip = be_clipboard->Data()))
            clip->FindData("text/plain", B_MIME_TYPE,(const void **)&text, &textLen);
            printf(text);
    be_clipboard->Unlock();
    }
}
