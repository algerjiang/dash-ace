# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashAceEditor(Component):
    """A DashAceEditor component.
Dash component wraps up react-ace editor
https://github.com/securingsincity/react-ace

Keyword arguments:
- id (string; default 'ace-editor'): The ID used to identify this component in Dash callbacks.
- value (string; default ''): The value displayed in the input.
- className (string; optional): Often used with CSS to style elements with common properties.
- placeholder (string; default 'Type code here ...'): Placeholder text to be displayed when editor is empty
- mode (string; default 'python'): Language for parsing and code highlighting
- theme (string; default 'monokai'): Theme to use
- fontSize (number; default 20): Font size
- showGutter (boolean; default True): Show gutter
- showPrintMargin (boolean; default True): Show print margin
- highlightActiveLine (boolean; default True): Highlight active line
- cursorStart (number; default 1): The location of the cursor
- wrapEnabled (boolean; default False): Wrapping lines
- readOnly (boolean; default False): Make the editor read only
- minLines (number; optional): Minimum number of lines to be displayed
- maxLines (number; optional): Maximum number of lines to be displayed
- enableBasicAutocompletion (boolean; default False): Enable basic autocompletion
- enableLiveAutocompletion (boolean; default False): Enable live autocompletion
- enableSnippets (boolean; default False): Enable snippets
- tabSize (number; default 4): Tab size
- debounceChangePeriod (number; optional): A debounce delay period for the onChange event
- editorProps (dict; default { $blockScrolling: Infinity}): Properties to apply directly to the Ace editor instance
- setOptions (dict; optional): Options to apply directly to the Ace editor instance
- keyboardHandler (string; optional): Key binding mode to set, e.g., vim or emacs
- commands (list; optional): New commands to add to the editor
- annotations (list; optional): Annotations to show in the editor, i.e., [{row:0, column:2, type:'error', text: 'some error'}
- markers (list; optional): Markers to show in the editor
- style (dict; optional): camelCased properties"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, className=Component.UNDEFINED, placeholder=Component.UNDEFINED, mode=Component.UNDEFINED, theme=Component.UNDEFINED, fontSize=Component.UNDEFINED, showGutter=Component.UNDEFINED, showPrintMargin=Component.UNDEFINED, highlightActiveLine=Component.UNDEFINED, cursorStart=Component.UNDEFINED, wrapEnabled=Component.UNDEFINED, readOnly=Component.UNDEFINED, minLines=Component.UNDEFINED, maxLines=Component.UNDEFINED, enableBasicAutocompletion=Component.UNDEFINED, enableLiveAutocompletion=Component.UNDEFINED, enableSnippets=Component.UNDEFINED, tabSize=Component.UNDEFINED, debounceChangePeriod=Component.UNDEFINED, editorProps=Component.UNDEFINED, setOptions=Component.UNDEFINED, keyboardHandler=Component.UNDEFINED, commands=Component.UNDEFINED, annotations=Component.UNDEFINED, markers=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'value', 'className', 'placeholder', 'mode', 'theme', 'fontSize', 'showGutter', 'showPrintMargin', 'highlightActiveLine', 'cursorStart', 'wrapEnabled', 'readOnly', 'minLines', 'maxLines', 'enableBasicAutocompletion', 'enableLiveAutocompletion', 'enableSnippets', 'tabSize', 'debounceChangePeriod', 'editorProps', 'setOptions', 'keyboardHandler', 'commands', 'annotations', 'markers', 'style']
        self._type = 'DashAceEditor'
        self._namespace = 'dash_ace'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'value', 'className', 'placeholder', 'mode', 'theme', 'fontSize', 'showGutter', 'showPrintMargin', 'highlightActiveLine', 'cursorStart', 'wrapEnabled', 'readOnly', 'minLines', 'maxLines', 'enableBasicAutocompletion', 'enableLiveAutocompletion', 'enableSnippets', 'tabSize', 'debounceChangePeriod', 'editorProps', 'setOptions', 'keyboardHandler', 'commands', 'annotations', 'markers', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashAceEditor, self).__init__(**args)