TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    problem1.cpp \
    problem2.cpp \
    linkedlist.cpp \
    queue.cpp \
    node.cpp

include(deployment.pri)
qtcAddDeployment()

HEADERS += \
    problem1.h \
    problem2.h \
    linkedlist.h \
    queue.h \
    node.h

