# PyVi
A python module with various functions to help with managing Vital Presets and directories

# Documentation

## getPreset(_filePath, returnType = {}_)
Used to get preset data from a file path
- `filePath` specifies the preset file to get; can only be a valid filepath string
- `returnType` specifies how you want the preset returned:
  - Entering a `dict` object or the string `'dict'` or `'dictionary'` **will return the preset data in a `dict`**
  - Entering a `str` object, that is not `'dict'` of `'dictionary'` or the string `'str'` or `'string'` **will return the preset data in a `str`**
  - If nothing is entered, it the default return type will be a `dict`

## writePreset(_filePath, data, passExists = False, prettyFile = True, indent = 4_)
Used to write data to files with formatting capabilities
- `filePath` specifies where the preset should be written; can only be a valid filepath string
- `data` specifies what will be writen; can be anything JSON encodable
- `passExists` when `True` will not write a file if it already exists; can only be a `boolean` object, defaults to `False`
- `prettyFile` when `True` will JSON format the entered `data` with an indent of `indent`; can only be a `boolean` object, defaults to `True`
- `indent` specifies how many spaces = 1 tab when JSON encoding; can be any positive `int`, defaults to `4`
- **Returns nothing**

## addNameTag(preset, setTo)
Used to add the `'preset_name'` tag to Vital presets, which is commonly missing in older presets.
- `preset` specifies the data to append the `'preset_name'` tag to; can only be a `dict` object
- `setTo` specifies what to set the `'preset_name'` tag to; can only be a `str` object
- **Returns a `dict` as `preset` with the tag `preset_name:setTo`**

## incrementPath(path, appendEnd = True, addUnderscore = True)
Increments file or folder names until they don't exist in your file system
- `path` specifies the path to increment; should only be a file path or folder path to work as intended
- `appendEnd` specifies where to add the increment 
   - `True` will increment the end of the `path` 
   - `False` will increment the beginning of the `path`
- `addUnderscore` when `True` will add an underscore in between the increment and the path:
   - EX: `0_filePath` , `filePath_0`
- **Returns a `str` as the incremented `path` name**

## listPresets(dirPath, listNested = False, topDown = True)
Lists all `'.vital'` files in a given `dirPath`
- `dirPath` specifies where to look for the presets; can only be a valid directory path
- `listNestes` when `True` will get all `'.vital'` files in nested directories; can only be `boolean` object, defaults to `False`
- `topDown` when `True` will list the `'.vital'` presets in the order they appear in the file browser
- **Returns a `list` as the Vital presets in the given `dirPath`**

## dirToDict(dirPath, only = (False, ''), ignores = (False, ''))
Generates a `dict` object with the structure of a file system
- `dirPath` specifies which directory to convert; should only be a valid folder path
- `only` gets only the specified file extention:
   - `only[0]` specifies if you are looking for only a specific file extention; can only be `boolean` object, defaults to `False`
   - `only[1]` specifies what extention you're looking for, can only be `str` object, defaults to `''`
- `ignores` ignores only the specified file extention:
   - `ignores[0]` specifies if you are ignoring only a specific file extention; can only be `boolean` object, defaults to `False`
   - `ignores[1]` specifies what extention you're looking to ignore, can only be `str` object, defaults to `''`
- Returns a `dict` object with subdirs as basename keys and files as `['/files']`
