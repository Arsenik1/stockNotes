defmodule WebWeb.LayoutView do
  use WebWeb, :html

  def root(assigns) do
    ~H"""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <title>Stock Notes</title>
        <%= csrf_meta_tag() %>
      </head>
      <body>
        <%= @inner_content %>
      </body>
    </html>
    """
  end
end
