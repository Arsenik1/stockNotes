import Config

config :web, WebWeb.Endpoint,
  url: [host: "localhost"],
  render_errors: [view: WebWeb.ErrorView, accepts: ~w(html json), layout: false],
  pubsub_server: Web.PubSub,
  live_view: [signing_salt: "changeme"]

config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

config :phoenix, :json_library, Jason

import_config "#{config_env()}.exs"
