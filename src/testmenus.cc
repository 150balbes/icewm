#include "config.h"
#include "ywindow.h"
#include "ymenu.h"
#include "yaction.h"
#include "ylocale.h"
#include "yapp.h"

const char *ApplicationName = "testmenus";

class MenuWindow: public YWindow {
public:
    YMenu *menu;
    YMenu *submenu0;
    YMenu *submenu1;
    YMenu *submenu2;

    MenuWindow() {
        menu = new YMenu();
        YAction *actionNone = new YAction();

        submenu0 = new YMenu();
        submenu0->addItem("XML Tree", 0, 0, actionNone);
        submenu0->addItem("Text", 0, 0, actionNone);
        submenu0->addItem("Hex", 0, 0, actionNone);

        submenu1 = new YMenu();
        submenu1->addItem("Name", 0, 0, actionNone);
        submenu1->addItem("Size", 0, 0, actionNone);
        submenu1->addItem("Modified", 0, 0, actionNone);
        submenu1->addItem("Modified", 0, 0, actionNone);

        submenu2 = new YMenu();
        submenu2->addItem("Contents", 0, 0, actionNone);
        submenu2->addItem("Search", 0, 0, actionNone);
        submenu2->addSeparator();
        submenu2->addItem("About", 0, 0, actionNone);

        menu = new YMenu();
        menu->addItem("Open", 0, 0, submenu0);
        menu->addItem("Properties", 0, 0, actionNone);
        menu->addSeparator();
        menu->addItem("Help", 0, 0, submenu2);
        menu->addSeparator();
        menu->addItem("Cut", 0, 0, actionNone);
        menu->addItem("Copy", 0, 0, actionNone);
        menu->addItem("Paste", 0, 0, actionNone);
        menu->addItem("Delete", 0, 0, actionNone);
        menu->addSeparator();
        menu->addItem("Sort", 0, actionNone, submenu1);
        menu->addSeparator();
        menu->addItem("Close", 0, 0, actionNone);
    }

    void handleButton(const XButtonEvent &button) {
        if ((button.type == ButtonRelease) &&
            (button.button == 3))
        {
            menu->popup(this, 0, 0, button.x_root, button.y_root, -1, -1,
                        YPopupWindow::pfCanFlipVertical |
                        YPopupWindow::pfCanFlipHorizontal |
                        YPopupWindow::pfPopupMenu);
        }
    }
};

int main(int argc, char **argv) {
    YLocale locale;
    YApplication app(&argc, &argv);

    YWindow *w = new MenuWindow();
    w->setSize(200, 200);
    w->show();

    return app.mainLoop();
}
