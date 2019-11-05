```
SeqCompress
| README.md
|
└─── configurations # All 'default' configuration files
|     | logger.conf
|
└─── docs # All non-README documentation
|     | Folder Structure.md
|
└─── SeqCompress # Actual code (main folder is mostly for calling)
|     | libs.py # Exposes all lib python files.
|     | SeqCompress.py
|     |
|     └─── libs # All/most functional code
|           | lib_compress_algorithms.py
|           | lib_decompress_algorithms.py
|           | lib_logging.py
|           | lib_sequence_data.py
|
└─── tests # Tests for code
      | test_compress_algorithms.py
```