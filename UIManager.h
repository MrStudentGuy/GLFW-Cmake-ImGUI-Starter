//
// Created by Aryan on 3/18/24.
//

#ifndef UIMANAGER_H
#define UIMANAGER_H
#include <vector>

#include "UIWindow.h"


class UIManager {
public:
	static void RegisterUIWindow(UIWindow* window);
	static void RenderUIWindows();

private:
	static std::vector<UIWindow*> m_Windows;
};

#endif //UIMANAGER_H
