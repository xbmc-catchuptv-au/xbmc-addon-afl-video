#
#    AFL Video Kodi Add-on
#    Copyright (C) 2016 Andy Botting
#
#    AFL Video is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    AFL Video is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this add-on. If not, see <http://www.gnu.org/licenses/>.
#

import classes
import utils
import comm
import xbmc
import xbmcgui


def play(url):
    try:
        params = utils.get_url(url)
        if 'id' in params:
            video_id = params['id']
            v = comm.get_video(video_id)
        elif 'url' in params:
            # New style
            v = classes.Video()
            v.parse_xbmc_url(url)

        listitem = xbmcgui.ListItem(label=v.get_title(),
                                    iconImage=v.get_thumbnail(),
                                    thumbnailImage=v.get_thumbnail())
        listitem.addStreamInfo('video', v.get_xbmc_stream_info())
        listitem.setInfo('video', v.get_xbmc_list_item())

        xbmc.Player().play(v.get_url(), listitem)
    except:
        utils.handle_error('Unable to play video')
