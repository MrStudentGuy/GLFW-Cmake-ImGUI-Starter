//
// Created by Aryan on 3/18/24.
//

#ifndef UIWINDOW_H
#define UIWINDOW_H

class UIWindow {
public:
	virtual ~UIWindow() = default;
	virtual void Render() = 0;
};

#endif //UIWINDOW_H