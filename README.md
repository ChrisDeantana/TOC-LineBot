# Learn Japanese - TOC Project 2021

A Line bot based on a finite state machine to learn basic japanese skills

## Finite State Machine
![fsm](./img/show-fsm.png)

## How to use
The initial state is set to `user`.

### States
* user
* characters
* hiragana
* katakana
* hiragana_basic
* hiragana_dakuon
* hiragana_combo
* hiragana_smallnlongvowels
* katakana_basic
* katakana_dakuon
* katakana_combo
* katakana_smallnlongvowels
* vocabulary
* daynmonth
* fruit
* hobby



The user will be asked to choose from 『Characters』/『Vocabulary』/『FSM』

if the user choose 『Characters』

	There will be another options such as 『Hiragana』/『Katakana』
	
		Each 『Hiragana』/『Katakana』have their own options, which are『Basic』/『Dakuon』/『Combo』/『SL-Vowels』
		
			The corresponding images will then be shown
			
if the user choose 『Vocabulary』.

	There will be another options such as 『daynmonth』/『fruits』/『hobby』
	
		The corresponding images will then be shown
		
if the user choose 『FSM』.

	a FSM graph will be shown 



