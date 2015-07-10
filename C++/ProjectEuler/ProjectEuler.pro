TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    problem1.cpp

include(deployment.pri)
qtcAddDeployment()

HEADERS += \
    problem1.h

