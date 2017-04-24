# Batch Connect - FVWM Assets

A library used for building a desktop using [FVWM](http://fvwm.org/) (desktop
window manager for the X Window system).

It is broken out into multiple FVWM scripts:

| FVWM Script | Description                                 |
| ----------- | -----------                                 |
| decorations | window decorations & menu styles            |
| globalfeel  | set up major operating system modes         |
| startup     | hooks run at startup and on restart         |
| functions   | utility functions                           |
| bindings    | mouse, frame buttons, and keyboard bindings |
| menus       | dropdown & context menu definitions         |
| modules     | module definitions                          |

Allowing for easier management and customization. A set of icons are also
included for better looking windows.

## Bower Install

You can install this in any project using Bower:

```sh
bower install git://github.com/OSC/bc_fvwm_assets.git --save
```

## Specification

### FVWM_ROOT

All assets in this package look for dependencies in the specified `$FVWM_ROOT`
directory. This should be set to correspond to the included `template/`
directory.

See below for an example.

## Usage

A configuration file (e.g.: `fvwmrc`) is supplied when launching the `fvwm`
process. Your app should come with this configuration file and explicitly use
the assets provided here.

The config file would be launched in your app script as such:

```sh
# Path where you installed this project
BC_FVWM_ASSETS_DIR="/path/to/bc_fvwm_assets/template"

# Run the fvwm wrapper script with proper `$FVWM_ROOT` set
FVWM_ROOT="${BC_FVWM_ASSETS_DIR}" "${BC_FVWM_ASSETS_DIR}/fvwm_wrapper" -f /path/to/fvwmrc &
```

Note that we use the supplied wrapper script so that defaults get set
appropriately.

An example `fvwmrc` file could look like:

```
Read $[FVWM_ROOT]/fvwm/decorations
Read $[FVWM_ROOT]/fvwm/globalfeel
Read $[FVWM_ROOT]/fvwm/startup
Read $[FVWM_ROOT]/fvwm/functions
Read $[FVWM_ROOT]/fvwm/bindings
Read $[FVWM_ROOT]/fvwm/menus
Read $[FVWM_ROOT]/fvwm/modules
```

Feel free to add any FVWM syntax to this file to override any of the features
supplied by the asset scripts.

## Contributing

1. Fork it ( https://github.com/OSC/bc_fvwm_assets/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
