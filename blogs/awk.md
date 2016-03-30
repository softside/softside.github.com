awk一个神奇的工具

#### 处理样例

    2015-11-23 18:04:10,016 - 17928 - ERROR:process task error:TransportError(404,u'RemoteTransportException[[es21][inet[/10.10.3.76:9301]][indices:data/write/update]]; nested: DocumentMissingException[[listening_v2_201511][0] [buzz][buzz428776987]: document missing]; ')

#### awk语句

    more migrate_comment.log |grep TransportError |awk 'match($0, /\[buzz[0-9]+\]/) {print substr($0, RSTART + 5, RLENGTH - 6)}' >missing_id.txt
