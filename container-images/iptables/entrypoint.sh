#!/bin/sh
while true; do
    for i in /rules/*; do 
        grep '^ip rule' "$i" | while IFS= read -r line; do
            RULE="${line#'ip rule add '}"
            echo "Adding IP RULE: '$RULE'"
            if ! ip rule show | grep -q "$RULE"; then
                ip rule add $RULE
                echo "Rule Added!"
            else
                echo "Rule already exists!!!"
            fi
        done
        grep '^iptables' "$i" | while IFS= read -r line; do
            RULE="${line#'iptables -A '}"
            echo "Adding IPTABLES RULE: '$RULE'"
            if ! iptables -C $RULE; then
                iptables -A $RULE
                echo "Rule Added!"
            else
                echo "Rule already exists!!!"
            fi
        done
    done
    echo ""
    echo "Rules checks finished. Sleeping for 30s"
    echo ""
    sleep 30
done