#The Django template language: For Python programmers

This document explains the Django template system from a technical perspective – how it works and how to extend it. If you’re just looking for reference on the language syntax, see The Django template language.

If you’re looking to use the Django template system as part of another application – i.e., without the rest of the framework – make sure to read the configuration section later in this document.

	本文档从技术的角度解释django的模板系统，它是如何工作的，以及如何扩展它。如果只看语法，另有文档。
	如果你想单独使用这个模板系统，即不用框架的其他部门，要先阅读本文档的配置部分。


##Basics
A template is a text document, or a normal Python string, that is marked-up using the Django template language. A template can contain block tags or variables.
    
    一个模板是一个文本文件，或者python string对象，用模板语言标记的。一个模板包括block标签和变量。
    
A block tag is a symbol within a template that does something.
    
    block标签在模板中可以做某些事情的符号
This definition is deliberately vague. For example, a block tag can output content, serve as a control structure (an “if” statement or “for” loop), grab content from a database or enable access to other template tags.
Block tags are surrounded by "{%" and "%}".
    
    这个定义——————，比如，标签可以输出内容，提供控制结构（"if"或者“for"）,从数据库中获取数据，使其它标签可以访问（这里说的是load吧，呵呵）
    
    
    
A variable is a symbol within a template that outputs a value.
Variable tags are surrounded by "{{" and "}}".
    
    变量是可以模板中可以输出值的符号，变量前后有“{{”和“}}“。
A context is a "variable name" -> "variable value" mapping that is passed to a template.
A template renders a context by replacing the variable "holes" with values from the context and executing all block tags.
    
    context是传递给模板的变量名到变量值的映射。
    
    
    
    
    
    
    
    
    
    
###Configuring the template system in standalone mode
Note
>*This section is only of interest to people trying to use the template system as an output component in another application. If you're using the template system as part of a Django application, nothing here applies to you.*

Normally, Django will load all the configuration information it needs from its own default configuration file, combined with the settings in the module given in the DJANGO_SETTINGS_MODULE environment variable. But if you're using the template system independently of the rest of Django, the environment variable approach isn't very convenient, because you probably want to configure the template system in line with the rest of your application rather than dealing with settings files and pointing to them via environment variables.

To solve this problem, you need to use the manual configuration option described in Using settings without setting DJANGO_SETTINGS_MODULE. Simply import the appropriate pieces of the templating system and then, before you call any of the templating functions, call django.conf.settings.configure() with any settings you wish to specify. You might want to consider setting at least TEMPLATE_DIRS (if you're going to use template loaders), DEFAULT_CHARSET (although the default of utf-8 is probably fine) and TEMPLATE_DEBUG. If you plan to use the url template tag, you will also need to set the ROOT_URLCONF setting. All available settings are described in the settings documentation, and any setting starting with TEMPLATE_ is of obvious interest.

Using an alternative template language
The Django Template and Loader classes implement a simple API for loading and rendering templates. By providing some simple wrapper classes that implement this API we can use third party template systems like Jinja2 or Cheetah. This allows us to use third-party template libraries without giving up useful Django features like the Django Context object and handy shortcuts like render_to_response().

The core component of the Django templating system is the Template class. This class has a very simple interface: it has a constructor that takes a single positional argument specifying the template string, and a render() method that takes a Context object and returns a string containing the rendered response.

Suppose we're using a template language that defines a Template object with a render() method that takes a dictionary rather than a Context object. We can write a simple wrapper that implements the Django Template interface:

import some_template_language

    class Template(some_template_language.Template):
    	def render(self, context):
        	# flatten the Django Context into a single dictionary.
           	context_dict = {}
          	for d in context.dicts:
            	context_dict.update(d)
        	return super(Template, self).render(context_dict)
That's all that's required to make our fictional Template class compatible with the Django loading and rendering system!

The next step is to write a Loader class that returns instances of our custom template class instead of the default Template. Custom Loader classes should inherit from django.template.loader.BaseLoader and override the load_template_source() method, which takes a template_name argument, loads the template from disk (or elsewhere), and returns a tuple: (template_string, template_origin).

The load_template() method of the Loader class retrieves the template string by calling load_template_source(), instantiates a Template from the template source, and returns a tuple: (template, template_origin). Since this is the method that actually instantiates the Template, we'll need to override it to use our custom template class instead. We can inherit from the builtin django.template.loaders.app_directories.Loader to take advantage of the load_template_source() method implemented there:

from django.template.loaders import app_directories
class Loader(app_directories.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, template_dirs)
        template = Template(source)
        return template, origin
Finally, we need to modify our project settings, telling Django to use our custom loader. Now we can write all of our templates in our alternative template language while continuing to use the rest of the Django templating system.
