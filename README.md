# EasyAI-OpenAI_api
一款基于OpenAI的api编写的桌面应用

<p align="center">
<a href="https://github.com/EdwardLA1127/EasyAI-OpenAI_api" target="_blank">
<img alt="macOS" src="https://img.shields.io/badge/-macOS-black?style=flat-square&logo=apple&logoColor=white" />
</a>

<a href="https://github.com/EdwardLA1127/EasyAI-OpenAI_api" target="_blank">
<img alt="Windows" src="https://img.shields.io/badge/-Windows-blue?style=flat-square&logo=windows&logoColor=white" />
</a>

<a href="https://github.com/EdwardLA1127/EasyAI-OpenAI_api" target="_blank">
<img alt="Linux" src="https://img.shields.io/badge/-Linux-yellow?style=flat-square&logo=linux&logoColor=white" />
</a>
</p>


如果你想进一步更新EasyAI，并根据你自己的需要添加你需要的功能或者根据你自己的喜好修改UI界面，请看下面的文件介绍：

为什么不用TypeScript? (当然是因为我没学过，不想学了)
大家应该普遍对python会比较熟悉，方便大家根据自己需要去定制化。

## application
Windows: 由py3exe (cx_Freeze) 将sourceCode里面的py脚本打包成的可在Windows平台下运行的exe程序。

## py3exe
一旦你编辑好了你的sourceCode，你可以在py3exe文件夹中的py3exe.py中定义好你的sourceCode的路径以及安装好的cx_Freeze的路径 
随后运行py3exe.py，它会在application文件夹中生成打包好的可在Windows平台下运行的exe程序。

## sourceCode
根据你的需要去修改功能或者添加功能

## UI
根据你的喜好去调整UI界面并将其添加到你的sourcecode中，基于PyQt6
