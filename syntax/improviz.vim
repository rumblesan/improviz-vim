if exists("b:current_syntax")
    finish
endif

set list
set listchars=tab:\ ▸

syntax keyword improvizKeyword times with
syntax keyword improvizKeyword if else elif

syntax match improvizOperator "\v\*"
syntax match improvizOperator "\v/"
syntax match improvizOperator "\v\+"
syntax match improvizOperator "\v-"
syntax match improvizOperator "\v\^"
syntax match improvizOperator "\v\%"
syntax match improvizOperator "\v\="
highlight link improvizOperator Operator

syntax match improvizLambda "\v\=\>"
highlight link improvizLambda Special

syntax match improvizNumber "\v\d+"
syntax match improvizFloat "\v\d+\.\d+"
highlight link improvizFloat Number
highlight link improvizNumber Number

syntax match improvizComment "\v#.*$"
highlight link improvizComment Comment

highlight link improvizKeyword Keyword

let b:current_syntax = "improviz"
