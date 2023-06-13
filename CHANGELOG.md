## Changelog

### Version 2.3
- App is live and can be accessed publicly.

### Version 2.2
- UI Refinements
    - Fixed bug which hides all the messages when loading.

### Version 2.1
- Included a cache for permanantly storing user prompts so the responses for the same prompts can be extracted without an API call
making it cost efficient and faster

### Version 2.0 (June 2023)
- Restructured the codebase
- Removed dependency on the previously cloned open source repository which consisted of a deep learning algorithm to train a dataset.
- Updated the chatbot to rely exclusively on the OpenAI algorithm for response generation.
- This change was made to address
    1. The large dependency size caused by the dependencies of the open source repository which restricted me from hosting the application.
    2. Simplify the codebase.
    3. Leverage a larger dataset for improved response quality.
- Tested using the ChatterBot 1.0.4 library for response generation to address the issues but decided not to integrate it due to the poor quality of responses which generated inaccurate and inconsistent responses.

### Version 1.0 (May 2023)
- Initial Release of the application


