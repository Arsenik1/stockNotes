defmodule WebWeb.Endpoint do
  use Phoenix.Endpoint, otp_app: :web

  socket "/live", Phoenix.LiveView.Socket

  plug Plug.Static,
    at: "/",
    from: :web,
    gzip: false,
    only: ~w(assets images favicon.ico robots.txt)

  if Application.compile_env(:web, :dev_routes) do
    plug Phoenix.LiveDashboard.RequestLogger,
      param_key: "request_logger",
      cookie_key: "request_logger"
  end

  plug Plug.RequestId
  plug Plug.Telemetry, event_prefix: [:web, :endpoint]

  plug Plug.Parsers,
    parsers: [:urlencoded, :multipart, :json],
    pass: ["*/*"],
    json_decoder: Phoenix.json_library()

  plug Plug.MethodOverride
  plug Plug.Head
  plug Plug.Session, store: :cookie, key: "_web_key", signing_salt: "change"

  plug WebWeb.Router
end
