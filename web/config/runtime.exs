import Config

if config_env() == :prod do
  config :web, WebWeb.Endpoint,
    http: [
      ip: {0, 0, 0, 0},
      port: String.to_integer(System.get_env("PORT") || "4000")
    ]
end
