//
// Created by Aryan on 3/18/24.
//

#ifndef HELLOWORLD_H
#define HELLOWORLD_H

#include "../UIManager.h"
#include "../UIWindow.h"

class HelloWorldWindow : public UIWindow {
public:
	HelloWorldWindow()
	{
		UIManager::RegisterUIWindow(this);
	}

	void Render() override;
};



#endif //HELLOWORLD_H
