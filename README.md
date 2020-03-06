# Improviz Vim Plugin

A vim plugin to allow interaction with [Improviz](https://github.com/rumblesan/improviz). Will only work on files with the `.pz` extention.

**NOTE: Requires a version of vim with python support! You may also need to `:UpdateRemotePlugins` after installing**

## Functionality

### Commands

* `:ImprovizSend`: Sends the content of the current buffer to a running improviz instance.
* `:ImprovizToggleText`: Turns the improviz text display on or off.
* `:ImprovizNudgeBeat amount`: Changes the improviz Nudge value by amount.

### Functions

All the commands are also available as functions.

* `ImprovizSend()`: Sends the content of the current buffer to a running improviz instance.
* `ImprovizToggleText()`: Turns the improviz text display on or off.
* `ImprovizNudgeBeat(amount)`: Changes the improviz Nudge value by amount.

## Licence

Unlicence
