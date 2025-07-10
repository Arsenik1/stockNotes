# Web Interface for StockNotes

This Phoenix LiveView application replicates the original Python features using the existing `short_term` and `long_term` folders for storage.

## Setup

1. Install Elixir and Erlang.
2. Fetch dependencies:

   ```bash
   mix deps.get
   ```

3. Start the server with:

   ```bash
   mix phx.server
   ```

The application expects the `short_term` and `long_term` directories to be in the project root (one level above this `web` folder). Notes are appended to the same text files used by the Python version.
