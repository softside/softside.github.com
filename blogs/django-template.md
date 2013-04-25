This is the Django template system.
===
How it works:
---
The Lexer.tokenize() function converts a template string (i.e., a string containing
markup with custom template tags) to tokens, which can be either plain text
(TOKEN_TEXT), variables (TOKEN_VAR) or block statements (TOKEN_BLOCK).


	Lexer.tokenize()这个函数可以把字符串分为4种类型（变量，区块，注释，还是文本）的token。


The Parser() class takes a list of tokens in its constructor, and its parse()
method returns a compiled template -- which is, under the hood, a list of
Node objects.

	这个就是生成node了，

Each Node is responsible for creating some sort of output -- e.g. simple text
(TextNode), variable values in a given context (VariableNode), results of basic
logic (IfNode), results of looping (ForNode), or anything else. The core Node
types are TextNode, VariableNode, IfNode and ForNode, but plugin modules can
define their own custom node types.

Each Node has a render() method, which takes a Context and returns a string of
the rendered node. For example, the render() method of a Variable Node returns
the variable's value as a string. The render() method of an IfNode returns the
rendered output of whatever was inside the loop, recursively.

The Template class is a convenient wrapper that takes care of template
compilation and rendering.



Sample code:
----
	
	from django import template
	s = u'<html>{% if test %}<h1>{{ varvalue }}</h1>{% endif %}</html>'
    t = template.Template(s)

t is now a compiled template, and its render() method can be called multiple
times with multiple contexts

	c = template.Context({'test':True, 'varvalue': 'Hello'})
	t.render(c)
output:

    "<html><h1>Hello</h1></html>"
    
change value:
    
    c = template.Context({'test':False, 'varvalue': 'Hello'})
    t.render(c)
out_put:

     u'<html></html>'

#compile_string

	def compile_string(template_string, origin):                                                         
      """Compiles template_string into NodeList ready for rendering"                                           
	    if settings.TEMPLATE_DEBUG:                                                                                    
    	    from debug import DebugLexer, DebugParser                                                                  
        	lexer_class, parser_class = DebugLexer, DebugParser                                                        
    	else:                                                                                                          
        	lexer_class, parser_class = Lexer, Parser                                                                  
    	lexer = lexer_class(template_string, origin)                                                                   
    	parser = parser_class(lexer.tokenize())                                                                        
    	return parser.parse()      


这个函数是一个很重要的函数，她结合Template类，Lexer类, Parser类，最后返回一个nodelist的list




#结论

核心流程：读取文件，获取文件内容，根据tag_re把string分为token的list，



这里的类是真不少啊：
	
	class FilterExpression(object):
	
	
	
	
	
	