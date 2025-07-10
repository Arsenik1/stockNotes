defmodule WebWeb do
  def controller do
    quote do
      use Phoenix.Controller, namespace: WebWeb
      import Plug.Conn
      alias WebWeb.Router.Helpers, as: Routes
    end
  end

  def live_view do
    quote do
      use Phoenix.LiveView,
        layout: {WebWeb.LayoutView, :root}
    end
  end

  def live_component do
    quote do
      use Phoenix.LiveComponent
    end
  end

  def html do
    quote do
      use Phoenix.Component
      import Phoenix.HTML
      alias WebWeb.Router.Helpers, as: Routes
    end
  end

  def router do
    quote do
      use Phoenix.Router
      import Phoenix.LiveView.Router
    end
  end

  def channel do
    quote do
      use Phoenix.Channel
    end
  end

  defmacro __using__(which) when is_atom(which) do
    apply(__MODULE__, which, [])
  end
end
