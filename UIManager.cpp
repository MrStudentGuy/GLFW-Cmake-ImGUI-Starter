//
// Created by Aryan on 3/18/24.
//

#include "UIManager.h"

std::vector<UIWindow*> UIManager::m_Windows;

void UIManager::RegisterUIWindow(UIWindow* window)
{
	m_Windows.push_back(window);
}

void UIManager::RenderUIWindows()
{
	for (UIWindow* window : m_Windows) {
		window -> Render();
	}
}


