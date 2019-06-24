#!/usr/bin/env python

# import ipdb
import argparse
import requests


parser = argparse.ArgumentParser()

parser.add_argument('-u', nargs=1, help="povide github user", required=True)
parser.add_argument('-r', nargs=1, help="provide github repo", required=True)
parser.add_argument('-t', nargs=1, help="provide github token", required=True)
parser.add_argument('-i', nargs=1, type=int,
                    help="show only PR with specific ID")
state = parser.add_mutually_exclusive_group()
state.add_argument('-o', help="show only open PR's", action='store_true')
state.add_argument('-c', help="show only closed PR's", action='store_true')
parser.add_argument('-ttl', help="show PR's title",
                    action='store_true')
parser.add_argument('-pru', help="show PR's user who opened",
                    action='store_true')
parser.add_argument('-dsc', help="show PR's descriptions", action='store_true')
parser.add_argument('-lab', help="show PR's labels", action='store_true')
parser.add_argument('-cd', help="show PR's creation or/and close date",
                    action='store_true')


parser.add_argument('-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()


def load_data(url, params):
    token = args.t[0]
    header = {'Authorization': 'token {}'.format(token)}
    while True:
        # ipdb.set_trace()
        r = requests.get(url, params=params, headers=header)
        body = r.json()
        if len(body) > 0:
            for data in body:
                yield data
            params["page"] += 1
        else:
            break


parameters = {
    'page': 1,
    'per_page': 100,
    'sort': 'updated',
    'direction': 'desc',
    'state': 'all',
}

repo_name = args.u[0] + '/' + args.r[0]
url = 'https://api.github.com/repos/' + repo_name + '/pulls'

if args.o:
    parameters.update({'state': 'open'})
if args.c:
    parameters.update({'state': 'closed'})

ttc = 0
for p in load_data(url, parameters):
    output = {}

    if args.i:
        if p.get('id') != args.i[0]:
            continue

    if args.ttl:
        output.update({'Title:': p.get('title')})
    if args.pru:
        output.update({'User:': p.get('user').get('login')})
    if args.dsc:
        output.update({'Description:': p.get('description')})
    if args.lab:
        output.update({'Label': p.get('label')})
    if args.cd:
        output.update({'Created_at:': p.get('created_at')})
        if args.c:
            output.update({'Closed_at:': p.get('closed_at')})

    if len(output):
        print('\n'.join('{}\t{}'.format(k, v) for k, v in output.items()))
        print('\n')
    ttc += 1

print('Total:', ttc)
