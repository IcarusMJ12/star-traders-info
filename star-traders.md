# Star Traders Database Diving

## Factions

```
#define FACTION_DEVALTOS 1
#define FACTION_CADAR 2
#define FACTION_RYCHART 3
#define FACTION_THULUN 4
#define FACTION_JAVAT 5
#define FACTION_STEELSONG 6
#define FACTION_MOKLUMNUE 7
#define FACTION_ALTAMESA 8
#define FACTION_ZENRIN 9
```


### Faction Ship Components

```sqlite3
select componentname as name, factionid as faction from shipcomponent where factionid > 0 and factionid < 10 order by faction;
```

|              name               | faction |
|---------------------------------|---------|
| ECCM Screen Matrix 4            | 1       |
| EVA Deck 4                      | 1       |
| Fuel-Cargo Hold 4               | 1       |
| Grand Lux Suites                | 1       |
| Quad-Goltha Scanner             | 1       |
| ECCM Screen Matrix 5            | 1       |
| Fuel-Cargo Hold 5               | 1       |
| Battle Launch Bay               | 1       |
| ECCM Screen Matrix 6            | 1       |
||
| Cerulean Tri-Arc                | 2       |
| Cadonya Buster Array            | 2       |
| Interlocking Sensor Matrix 4    | 2       |
| Battle Prow 4                   | 2       |
| Shielded Barracks 4             | 2       |
| M7000 Void Engine: Behemoth     | 2       |
| Battle Prow 5                   | 2       |
| Warhammer Hyperwarp Drive       | 2       |
| Targetlock Matrix 5             | 2       |
||
| Depth Scanner Omega             | 3       |
| Depth Scanner Omega-X           | 3       |
| Multi-Signal Array              | 3       |
| M6000 Void Engine: Behemoth     | 3       |
| Sig Veil Field                  | 3       |
| Redlight Goltha Scanner         | 3       |
| Redlance Goltha Scanner         | 3       |
| Scout-Stealth Bridge 5          | 3       |
| Peak Velocity Matrix 4          | 3       |
| Quturaan Phase Inflector 3      | 3       |
||
| Orbital Fuel Scoop 4            | 4       |
| Salvage Bay 4                   | 4       |
| M5000 Void Engine: Behemoth     | 4       |
| Armored Cargo Hold 4            | 4       |
| Lion Mass Reducer 4             | 4       |
| Interlocking Sensor Matrix 5    | 4       |
| Warhammer Hyperwarp Drive       | 4       |
| Salvage Bay 5                   | 4       |
| Armored Salvage Bay 5           | 4       |
| Interlock Matrix 5              | 4       |
| Tactician's Annex               | 4       |
| Katteduun Phase Inflector 4     | 4       |
| Orbital Fuel Scoop 5            | 4       |
| Advanced Hangar Bay             | 4       |
| Interlocking Sensor Matrix 6    | 4       |
| Salvage Bay 6                   | 4       |
||
| Resource Processor              | 5       |
| Javat Mechi-Reaper              | 5       |
| Defense Pattern Matrix 4        | 5       |
| Hull Plating 4                  | 5       |
| M3400 Void Engine: Behemoth     | 5       |
| Hull Plating 5                  | 5       |
| Water-Fuel Reclamation 2        | 5       |
| Hauler Hold                     | 5       |
| Water-Fuel Reclamation 3        | 5       |
| Performance Hyperwarp Drive     | 5       |
| Water-Fuel Reclamation 4        | 5       |
| Water-Fuel Reclamation 5        | 5       |
| Water-Fuel Reclamation 6        | 5       |
||
| Hyperion Exo-Suits              | 6       |
| Hazuk Duo-Arc                   | 6       |
| Boarding Assault System 4       | 6       |
| M2400 Void Engine: Behemoth     | 6       |
| Interrogation Chamber           | 6       |
| Interrogation Ward              | 6       |
| Railtrak Guidance Matrix 4      | 6       |
| Scout-Vanguard Bridge 5         | 6       |
| Performance Hyperwarp Drive     | 6       |
| Warden's Annex                  | 6       |
||
| Targeting Matrix 4              | 7       |
| Cargo Hold 5                    | 7       |
| M9000 Void Engine: Behemoth     | 7       |
| Warhammer Hyperwarp Drive       | 7       |
| Capital Freighter Bridge 5      | 7       |
| Performance Hyperwarp Drive     | 7       |
| Armored Cargo Hold 5            | 7       |
||
| Mesa Radiate-Seal               | 8       |
| Reinforced Fuel Tank            | 8       |
| Reinforced Fuel Pod             | 8       |
| M8000 Void Engine: Behemoth     | 8       |
| Battle Bridge                   | 8       |
| Hawk Mass Reducer 4             | 8       |
| Battle Bridge 2                 | 8       |
| Warhammer Hyperwarp Drive       | 8       |
| Battle Bridge 3                 | 8       |
| Scout-Skirmish Bridge 5         | 8       |
| Capital Carrier Bridge 5        | 8       |
| Navigation Annex                | 8       |
| Warhawk Launch Bay              | 8       |
| Joint Precision Launch System 3 | 8       |
| Battle Bridge 4                 | 8       |
||
| Armored Officer Suites          | 9       |
| Armored Bulkheads 5             | 9       |
| Reinforced Structures 5         | 9       |
| C-Tak Interceptor System 4      | 9       |
| Scout-Hauler Bridge 5           | 9       |
| Compact Capital Bridge 4        | 9       |
| Engineering Annex               | 9       |
| Performance Hyperwarp Drive     | 9       |
| Fuel Helix Coil 4               | 9       |
| Fuel Helix Coil 5               | 9       |

## Ship Components - Core

### Bridges

Scout bridges (size 1) carry 3 officers, others only 1.

Capital carrier bridge also offers 25 storage and fuel.

Other effects:

```sqlite3
select effectName as name, craftmovestatus as craftmove, rangedattackbonus as attack, defensivebonus as def, radres, voidres, movebonus as move, escapebonus as "escape", cloakbonus as cloak, enginesafety as safety from shipeffect where _id in (select shipeffectid from shipcomponent where componenttype = 1 and factionid < 10 and shipeffectid > 0);
```

|           name           | craftmove | attack | def | radRes | voidRes | move | escape | cloak | safety |
|--------------------------|-----------|--------|-----|--------|---------|------|--------|-------|--------|
| Battle Bridge            | 0         | 10     | 0   | 10     | 10      | 0    | 0      | 0     | 0      |
| Battle Bridge 2          | 0         | 10     | 0   | 12     | 12      | 4    | 0      | 0     | 0      |
| Battle Bridge 3          | 0         | 12     | 0   | 14     | 14      | 4    | 0      | 0     | 0      |
| Scout-Stealth Bridge 5   | 0         | 0      | 0   | 0      | 0       | 0    | 0      | 10    | 0      |
| Scout-Skirmish Bridge 5  | 0         | 10     | 0   | 0      | 0       | 0    | 0      | 0     | 0      |
| Scout-Hauler Bridge 5    | 0         | 0      | 0   | 0      | 0       | 0    | 10     | 0     | 0      |
| Capital Carrier Bridge 5 | 12        | 0      | 0   | 0      | 0       | 0    | 0      | 0     | 0      |
| Scout-Vanguard Bridge 5  | 0         | 0      | 4   | 0      | 0       | 0    | 0      | 0     | 0      |
| Compact Capital Bridge 4 | 0         | 0      | 0   | 0      | 0       | 0    | 0      | 0     | 1      |


```sqlite3
select componentsize as s, componentname as name, skpilot as pil, skshipops as ops, skelectronics as ele, sknavigation as nav, jumpcost as jmp, armorbonus as arm, deflectionbonus as shl, mass, factionid as faction from shipcomponent where componenttype = 1 and factionid < 10 order by s;
```

| s |            name            | pil | ops | ele | nav | jmp | arm | shl | mass | faction |
|---|----------------------------|-----|-----|-----|-----|-----|-----|-----|------|---------|
| 1 | Scout Bridge               | 4   | 2   | 3   | 3   | 0   | 0   | 0   | 100  | 0       |
| 1 | Scout Bridge 2             | 5   | 3   | 4   | 4   | 0   | 0   | 1   | 100  | 0       |
| 1 | Scout Bridge 3             | 6   | 3   | 4   | 4   | 1   | 1   | 2   | 100  | 0       |
| 1 | Scout Bridge 4             | 7   | 4   | 5   | 5   | 3   | 3   | 3   | 100  | 0       |
| 1 | Scout-Stealth Bridge 5     | 7   | 4   | 8   | 6   | 3   | 3   | 3   | 100  | 3       |
| 1 | Scout-Skirmish Bridge 5    | 8   | 4   | 6   | 6   | 4   | 4   | 4   | 100  | 8       |
| 1 | Scout-Hauler Bridge 5      | 8   | 4   | 5   | 8   | -5  | 2   | 2   | -100 | 9       |
| 1 | Scout-Vanguard Bridge 5    | 6   | 5   | 8   | 6   | 2   | 2   | 2   | 100  | 6       |
||
| 2 | Bridge                     | 5   | 3   | 4   | 5   | 0   | 0   | 0   | 300  | 0       |
| 2 | Bridge 2                   | 6   | 3   | 5   | 5   | 0   | 0   | 0   | 300  | 0       |
| 2 | Bridge 3                   | 6   | 4   | 5   | 6   | 0   | 1   | 0   | 300  | 0       |
| 2 | Bridge 4                   | 7   | 4   | 5   | 7   | 0   | 1   | 0   | 300  | 0       |
| 2 | Battle Bridge              | 6   | 3   | 4   | 6   | 4   | 2   | 0   | 250  | 8       |
| 2 | Battle Bridge 2            | 8   | 4   | 5   | 8   | 3   | 2   | 0   | 250  | 8       |
| 2 | Battle Bridge 3            | 9   | 4   | 6   | 8   | 4   | 2   | 0   | 250  | 8       |
| 2 | Battle Bridge 4            | 9   | 4   | 6   | 8   | 4   | 2   | 0   | 250  | 8       |
||
| 3 | Capital Bridge             | 9   | 5   | 8   | 8   | 0   | 0   | 0   | 600  | 0       |
| 3 | Capital Bridge 2           | 9   | 5   | 9   | 9   | 0   | 0   | 0   | 600  | 0       |
| 3 | Capital Bridge 3           | 9   | 6   | 10  | 9   | 0   | 1   | 0   | 600  | 0       |
| 3 | Capital Bridge 4           | 10  | 6   | 10  | 10  | 1   | 1   | 0   | 600  | 0       |
| 3 | Capital Freighter Bridge 5 | 9   | 5   | 9   | 9   | -5  | 0   | 0   | 600  | 7       |
| 3 | Capital Carrier Bridge 5   | 9   | 5   | 11  | 9   | 5   | 0   | 0   | 600  | 8       |
| 3 | Compact Capital Bridge 4   | 9   | 6   | 10  | 8   | 0   | 0   | 0   | 480  | 9       |


### Engines

```sqlite3
select
  componentname as name, skpilot as pil, skshipops as ops, skelectronics as ele, sknavigation as nav, armorbonus as arm, deflectionbonus as shl, mass, factionid as faction,
  actionpoints as ap, movecost as rngchg, shipspeed as spd, shipagile as agi, mapfuelcost as au, combatfuelcost as fuel, safetyrating as sfty
from shipcomponent
inner join shipengine on shipcomponent.shipengineid = shipengine._id
where componenttype = 3 and factionid < 10 order by name;
```

|             name              | pil | ops | ele | nav | arm | shl | mass | faction | ap | rngchg | spd | agi | au | fuel | sfty |
|-------------------------------|-----|-----|-----|-----|-----|-----|------|---------|----|--------|-----|-----|----|------|------|
| M2400 Void Engine: Balanced   | 7   | 6   | 6   | 2   | 3   | 1   | 200  | 0       | 8  | 3      | 27  | 27  | 2  | 0    | 12   |
| M2400 Void Engine: Behemoth   | 8   | 6   | 6   | 2   | 7   | 2   | 200  | 6       | 9  | 3      | 29  | 27  | 3  | 0    | 7    |
| M2400 Void Engine: Chaser     | 7   | 6   | 6   | 2   | 3   | 1   | 200  | 0       | 8  | 2      | 27  | 30  | 1  | 0    | 10   |
| M2400 Void Engine: Dual-Field | 7   | 6   | 6   | 2   | 3   | 1   | 100  | 0       | 8  | 3      | 27  | 27  | 2  | 0    | 12   |
| M2400 Void Engine: Longhaul   | 6   | 6   | 7   | 2   | 3   | 1   | 200  | 0       | 8  | 3      | 27  | 27  | 1  | 0    | 15   |
| M2400 Void Engine: Traveler   | 6   | 6   | 6   | 2   | 3   | 1   | 200  | 0       | 8  | 3      | 30  | 27  | 2  | 0    | 6    |
| M2400 Void Engine: Warhammer  | 6   | 6   | 6   | 2   | 3   | 2   | 200  | 0       | 9  | 3      | 27  | 28  | 3  | 0    | 7    |
||
| M3400 Void Engine: Balanced   | 8   | 8   | 7   | 2   | 2   | 0   | 400  | 0       | 8  | 3      | 24  | 24  | 2  | 0    | 12   |
| M3400 Void Engine: Behemoth   | 8   | 9   | 7   | 2   | 8   | 3   | 450  | 5       | 9  | 3      | 27  | 24  | 3  | 0    | 7    |
| M3400 Void Engine: Chaser     | 9   | 7   | 7   | 2   | 2   | 0   | 400  | 0       | 8  | 2      | 24  | 29  | 2  | 0    | 8    |
| M3400 Void Engine: Dual-Field | 8   | 8   | 7   | 2   | 2   | 0   | 200  | 0       | 8  | 3      | 24  | 24  | 2  | 0    | 12   |
| M3400 Void Engine: Longhaul   | 7   | 9   | 7   | 2   | 2   | 0   | 400  | 0       | 8  | 3      | 23  | 23  | 1  | 0    | 15   |
| M3400 Void Engine: Traveler   | 7   | 7   | 9   | 2   | 2   | 0   | 400  | 0       | 8  | 3      | 29  | 24  | 2  | 0    | 8    |
| M3400 Void Engine: Warhammer  | 7   | 9   | 7   | 2   | 2   | 2   | 450  | 0       | 9  | 3      | 24  | 26  | 3  | 0    | 7    |
||
| M5000 Void Engine: Balanced   | 9   | 9   | 6   | 0   | 0   | 0   | 700  | 0       | 8  | 4      | 19  | 19  | 2  | 0    | 10   |
| M5000 Void Engine: Behemoth   | 9   | 9   | 7   | 3   | 9   | 4   | 750  | 4       | 9  | 4      | 21  | 19  | 4  | 5    | 6    |
| M5000 Void Engine: Chaser     | 10  | 8   | 6   | 0   | 0   | 0   | 700  | 0       | 8  | 3      | 18  | 22  | 2  | 0    | 8    |
| M5000 Void Engine: Dual-Field | 9   | 9   | 6   | 0   | 0   | 0   | 450  | 0       | 8  | 4      | 19  | 19  | 2  | 0    | 10   |
| M5000 Void Engine: Longhaul   | 9   | 9   | 6   | 0   | 0   | 0   | 700  | 0       | 8  | 4      | 20  | 18  | 1  | 0    | 11   |
| M5000 Void Engine: Traveler   | 8   | 10  | 6   | 0   | 0   | 0   | 700  | 0       | 8  | 4      | 23  | 16  | 3  | 0    | 8    |
| M5000 Void Engine: Warhammer  | 9   | 9   | 7   | 1   | 1   | 2   | 750  | 0       | 9  | 4      | 19  | 20  | 4  | 4    | 6    |
||
| M6000 Void Engine: Balanced   | 11  | 9   | 8   | 0   | 0   | 0   | 1100 | 0       | 8  | 4      | 15  | 15  | 3  | 5    | 10   |
| M6000 Void Engine: Behemoth   | 11  | 9   | 8   | 3   | 10  | 5   | 1100 | 3       | 9  | 4      | 17  | 14  | 4  | 8    | 6    |
| M6000 Void Engine: Chaser     | 11  | 9   | 8   | 0   | 0   | 0   | 1100 | 0       | 8  | 3      | 13  | 18  | 2  | 4    | 7    |
| M6000 Void Engine: Dual-Field | 11  | 9   | 8   | 0   | 0   | 0   | 775  | 0       | 8  | 4      | 15  | 15  | 3  | 5    | 10   |
| M6000 Void Engine: Longhaul   | 10  | 11  | 7   | 0   | 0   | 0   | 1100 | 0       | 8  | 4      | 15  | 15  | 2  | 3    | 11   |
| M6000 Void Engine: Traveler   | 11  | 9   | 8   | 0   | 0   | 0   | 1100 | 0       | 8  | 4      | 19  | 13  | 3  | 4    | 8    |
| M6000 Void Engine: Warhammer  | 11  | 9   | 8   | 1   | 1   | 2   | 1100 | 0       | 9  | 4      | 15  | 16  | 4  | 6    | 6    |
||
| M7000 Void Engine: Balanced   | 11  | 9   | 8   | 0   | 0   | 0   | 1300 | 0       | 8  | 4      | 12  | 12  | 4  | 6    | 9    |
| M7000 Void Engine: Behemoth   | 12  | 10  | 10  | 3   | 11  | 6   | 1300 | 2       | 10 | 4      | 14  | 11  | 5  | 10   | 6    |
| M7000 Void Engine: Chaser     | 10  | 9   | 10  | 0   | 0   | 0   | 1300 | 0       | 8  | 3      | 10  | 14  | 3  | 5    | 7    |
| M7000 Void Engine: Dual-Field | 11  | 9   | 8   | 0   | 0   | 0   | 960  | 0       | 8  | 4      | 12  | 12  | 4  | 6    | 9    |
| M7000 Void Engine: Longhaul   | 12  | 10  | 9   | 0   | 0   | 0   | 1300 | 0       | 8  | 4      | 12  | 11  | 3  | 4    | 10   |
| M7000 Void Engine: Traveler   | 12  | 11  | 9   | 0   | 0   | 0   | 1300 | 0       | 8  | 4      | 15  | 9   | 4  | 8    | 8    |
| M7000 Void Engine: Warhammer  | 12  | 10  | 10  | 1   | 1   | 2   | 1300 | 0       | 10 | 4      | 12  | 13  | 5  | 8    | 6    |
||
| M8000 Void Engine: Balanced   | 14  | 12  | 11  | 0   | 0   | 0   | 1500 | 0       | 8  | 4      | 9   | 9   | 4  | 5    | 9    |
| M8000 Void Engine: Behemoth   | 14  | 12  | 12  | 4   | 12  | 7   | 1500 | 8       | 11 | 4      | 12  | 9   | 5  | 12   | 5    |
| M8000 Void Engine: Chaser     | 16  | 12  | 11  | 0   | 0   | 0   | 1500 | 0       | 8  | 3      | 10  | 12  | 4  | 2    | 6    |
| M8000 Void Engine: Dual-Field | 14  | 12  | 11  | 0   | 0   | 0   | 1020 | 0       | 8  | 4      | 9   | 9   | 4  | 5    | 9    |
| M8000 Void Engine: Longhaul   | 15  | 14  | 12  | 0   | 0   | 0   | 1500 | 0       | 8  | 4      | 10  | 6   | 3  | 4    | 9    |
| M8000 Void Engine: Traveler   | 14  | 13  | 9   | 0   | 0   | 0   | 1500 | 0       | 8  | 4      | 15  | 8   | 5  | 8    | 7    |
| M8000 Void Engine: Warhammer  | 14  | 12  | 12  | 2   | 1   | 2   | 1500 | 0       | 10 | 4      | 9   | 11  | 5  | 10   | 5    |
||
| M9000 Void Engine: Balanced   | 13  | 13  | 10  | 0   | 0   | 0   | 1750 | 0       | 8  | 4      | 9   | 9   | 4  | 5    | 8    |
| M9000 Void Engine: Behemoth   | 16  | 12  | 12  | 4   | 13  | 8   | 1750 | 7       | 11 | 4      | 11  | 9   | 5  | 14   | 4    |
| M9000 Void Engine: Chaser     | 15  | 14  | 10  | 0   | 0   | 0   | 1750 | 0       | 8  | 3      | 10  | 10  | 4  | 5    | 6    |
| M9000 Void Engine: Dual-Field | 14  | 12  | 10  | 0   | 0   | 0   | 1100 | 0       | 8  | 4      | 9   | 9   | 4  | 5    | 8    |
| M9000 Void Engine: Longhaul   | 15  | 15  | 10  | 0   | 0   | 0   | 1750 | 0       | 8  | 4      | 10  | 6   | 3  | 6    | 9    |
| M9000 Void Engine: Traveler   | 14  | 16  | 11  | 0   | 0   | 0   | 1750 | 0       | 8  | 4      | 15  | 8   | 5  | 8    | 6    |
| M9000 Void Engine: Warhammer  | 16  | 12  | 12  | 2   | 1   | 2   | 1750 | 0       | 10 | 4      | 9   | 10  | 5  | 12   | 4    |


### Hyperwarp Drives

Performance hyperwarp drives reduce jump time.

```sqlite3
select drivemass, componentname as name, skpilot as pil, skelectronics as ele, sknavigation as nav, jumpcost as jmp, armorbonus as arm, deflectionbonus as shl, mass, factionid as faction
from shipcomponent where componenttype = 9 and factionid < 10 order by drivemass, name;
```

| driveMass |            name             | pil | ele | nav | jmp | arm | shl | mass | faction |
|-----------|-----------------------------|-----|-----|-----|-----|-----|-----|------|---------|
| 2400      | Basic Hyperwarp Drive       | 0   | 2   | 6   | 14  | 0   | 1   | 200  | 0       |
| 2400      | Combat Hyperwarp Drive      | 2   | 3   | 7   | 18  | 1   | 4   | 190  | 0       |
| 2400      | Kickstarter Hyperwarp Drive | 0   | 3   | 7   | 12  | 1   | 2   | 200  | 0       |
| 2400      | Longhaul Hyperwarp Drive    | 0   | 3   | 8   | 10  | 0   | 1   | 200  | 0       |
| 2400      | Performance Hyperwarp Drive | 0   | 5   | 7   | 24  | 0   | 0   | 190  | 6       |
| 2400      | Warhammer Hyperwarp Drive   | 6   | 5   | 7   | 24  | 4   | 6   | 190  | 7       |
||
| 3400      | Basic Hyperwarp Drive       | 0   | 3   | 10  | 18  | 0   | 2   | 225  | 0       |
| 3400      | Combat Hyperwarp Drive      | 2   | 3   | 10  | 20  | 1   | 3   | 215  | 0       |
| 3400      | Kickstarter Hyperwarp Drive | 0   | 4   | 11  | 16  | 1   | 1   | 225  | 0       |
| 3400      | Longhaul Hyperwarp Drive    | 0   | 3   | 12  | 14  | 0   | 1   | 225  | 0       |
| 3400      | Performance Hyperwarp Drive | 0   | 5   | 8   | 26  | 0   | 0   | 215  | 5       |
| 3400      | Warhammer Hyperwarp Drive   | 6   | 5   | 8   | 26  | 4   | 6   | 215  | 8       |
||
| 5000      | Basic Hyperwarp Drive       | 0   | 3   | 12  | 22  | 0   | 0   | 225  | 0       |
| 5000      | Combat Hyperwarp Drive      | 3   | 2   | 12  | 25  | 2   | 3   | 215  | 0       |
| 5000      | Kickstarter Hyperwarp Drive | 0   | 4   | 13  | 20  | 1   | 0   | 225  | 0       |
| 5000      | Longhaul Hyperwarp Drive    | 0   | 4   | 14  | 18  | 0   | 0   | 225  | 0       |
| 5000      | Performance Hyperwarp Drive | 0   | 6   | 8   | 31  | 0   | 0   | 215  | 0       |
| 5000      | Warhammer Hyperwarp Drive   | 7   | 6   | 8   | 31  | 6   | 5   | 215  | 0       |
||
| 6000      | Basic Hyperwarp Drive       | 0   | 6   | 14  | 26  | 0   | 0   | 300  | 0       |
| 6000      | Combat Hyperwarp Drive      | 3   | 5   | 14  | 29  | 2   | 2   | 290  | 0       |
| 6000      | Kickstarter Hyperwarp Drive | 0   | 5   | 15  | 24  | 0   | 0   | 300  | 0       |
| 6000      | Longhaul Hyperwarp Drive    | 0   | 4   | 17  | 22  | 0   | 0   | 300  | 0       |
| 6000      | Performance Hyperwarp Drive | 0   | 7   | 10  | 35  | 0   | 0   | 290  | 0       |
| 6000      | Warhammer Hyperwarp Drive   | 7   | 7   | 10  | 35  | 6   | 5   | 290  | 0       |
||
| 7000      | Basic Hyperwarp Drive       | 0   | 5   | 15  | 28  | 0   | 0   | 500  | 0       |
| 7000      | Combat Hyperwarp Drive      | 4   | 4   | 15  | 32  | 3   | 2   | 480  | 0       |
| 7000      | Kickstarter Hyperwarp Drive | 0   | 6   | 16  | 26  | 1   | 1   | 500  | 0       |
| 7000      | Longhaul Hyperwarp Drive    | 0   | 7   | 18  | 25  | 0   | 0   | 500  | 0       |
| 7000      | Performance Hyperwarp Drive | 0   | 7   | 11  | 38  | 0   | 0   | 480  | 0       |
| 7000      | Warhammer Hyperwarp Drive   | 8   | 7   | 11  | 38  | 7   | 4   | 480  | 0       |
||
| 8000      | Basic Hyperwarp Drive       | 0   | 8   | 18  | 32  | 0   | 0   | 550  | 0       |
| 8000      | Combat Hyperwarp Drive      | 4   | 7   | 17  | 36  | 3   | 1   | 525  | 0       |
| 8000      | Kickstarter Hyperwarp Drive | 0   | 10  | 17  | 30  | 0   | 0   | 550  | 0       |
| 8000      | Longhaul Hyperwarp Drive    | 0   | 7   | 20  | 28  | 0   | 0   | 550  | 0       |
| 8000      | Performance Hyperwarp Drive | 0   | 8   | 13  | 42  | 0   | 0   | 525  | 9       |
| 8000      | Warhammer Hyperwarp Drive   | 8   | 8   | 13  | 42  | 7   | 4   | 525  | 2       |
||
| 9000      | Basic Hyperwarp Drive       | 0   | 10  | 19  | 36  | 0   | 0   | 750  | 0       |
| 9000      | Combat Hyperwarp Drive      | 4   | 8   | 19  | 40  | 3   | 1   | 725  | 0       |
| 9000      | Longhaul Hyperwarp Drive    | 0   | 8   | 21  | 30  | 0   | 0   | 750  | 0       |
| 9000      | Performance Hyperwarp Drive | 0   | 9   | 15  | 50  | 0   | 0   | 725  | 7       |
| 9000      | Warhammer Hyperwarp Drive   | 8   | 9   | 15  | 50  | 7   | 3   | 725  | 4       |


## Ship Components - Non-Core

### Cargo

```sqlite3
select componentsize as s, componentname as name, skpilot as pil, skshipops as ops, holdscargo as cargo, fuelbonus as fuel, jumpcost as jmp, armorbonus as arm, deflectionbonus as shl, mass, factionid as faction
from shipcomponent where componenttype = 2 and factionid < 10 order by s, cargo, name;
```

| s |         name         | pil | ops | cargo | fuel | jmp | arm | shl | mass | faction |
|---|----------------------|-----|-----|-------|------|-----|-----|-----|------|---------|
| 1 | Cargo-Fuel Pod       | 0   | 1   | 5     | 10   | 0   | 0   | 0   | 120  | 0       |
| 1 | Storage Cache        | 0   | 1   | 10    | 0    | 0   | 0   | 0   | 125  | 0       |
||
| 2 | Armored Storage      | 0   | 3   | 10    | 0    | 1   | 1   | 1   | 325  | 0       |
| 2 | Cargo-Fuel Storage   | 0   | 3   | 15    | 15   | 0   | 0   | 0   | 325  | 0       |
| 2 | Storage Hold         | 0   | 3   | 25    | 0    | 0   | 0   | 0   | 325  | 0       |
||
| 3 | Cargo Hold 1         | 0   | 2   | 25    | 40   | 0   | 0   | 0   | 625  | 0       |
| 3 | Cargo Hold 2         | 0   | 2   | 35    | 50   | 0   | 0   | 0   | 625  | 0       |
| 3 | Fuel-Cargo Hold 4    | 0   | 4   | 35    | 95   | 0   | 0   | 0   | 625  | 1       |
| 3 | Fuel-Cargo Hold 5    | 0   | 5   | 35    | 120  | 0   | 0   | 0   | 625  | 1       |
| 3 | Armored Cargo Hold 4 | 0   | 4   | 40    | 65   | 3   | 3   | 1   | 625  | 4       |
| 3 | Cargo Hold 3         | 0   | 4   | 40    | 60   | 0   | 0   | 0   | 625  | 0       |
| 3 | Cargo Hold 4         | 0   | 4   | 45    | 70   | 0   | 0   | 0   | 625  | 0       |
| 3 | Armored Cargo Hold 5 | 0   | 4   | 50    | 75   | 2   | 5   | 0   | 625  | 7       |
| 3 | Cargo Hold 5         | 0   | 4   | 50    | 75   | 2   | 0   | 0   | 625  | 7       |
| 3 | Armored Cargo Hold 6 | 0   | 6   | 60    | 75   | 2   | 6   | 0   | 625  | 0       |
| 3 | Cargo Hold 6         | 0   | 6   | 60    | 75   | 2   | 0   | 0   | 625  | 0       |
| 3 | Hauler Hold          | 0   | 5   | 65    | 40   | 2   | 0   | 3   | 625  | 5       |
| 3 | Cargo Hold 7         | 0   | 6   | 70    | 75   | 2   | 0   | 0   | 625  | 0       |
| 3 | Cargo Hold 8         | 0   | 7   | 80    | 80   | 2   | 0   | 0   | 625  | 0       |


#### Cargo and Fuel Combined

```sqlite3
select componentsize as size, componentname as name, holdscargo as cargo, fuelbonus as fuel from shipcomponent where factionid < 10 and (holdscargo > 0 or fuelbonus > 0) order by componentsize, holdscargo, fuelbonus;
```

| size |            name            | cargo | fuel |
|------|----------------------------|-------|------|
| 1    | Reactor Spike Module 1     | 0     | 5    |
| 1    | Reactor Spike Module 2     | 0     | 15   |
| 1    | Small Fuel Tank 1          | 0     | 20   |
| 1    | Reactor Spike Module 3     | 0     | 25   |
| 1    | Small Fuel Tank 2          | 0     | 26   |
| 1    | Small Fuel Tank 3          | 0     | 32   |
| 1    | Reinforced Fuel Pod        | 0     | 32   |
| 1    | Reactor Spike Module 4     | 0     | 35   |
| 1    | Small Fuel Tank 4          | 0     | 38   |
| 1    | Cargo-Fuel Pod             | 5     | 10   |
| 1    | Storage Cache              | 10    | 0    |
||
| 2    | EVA Deck 1                 | 0     | 5    |
| 2    | Orbital Fuel Scoop 1       | 0     | 10   |
| 2    | EVA Deck 2                 | 0     | 10   |
| 2    | Shielded Hangar Bay        | 0     | 10   |
| 2    | Reinforced Hangar Bay      | 0     | 10   |
| 2    | Fuel Helix Coil 2          | 0     | 10   |
| 2    | Reactive Hangar Bay        | 0     | 12   |
| 2    | Advanced Hangar Bay        | 0     | 12   |
| 2    | Fuel Helix Coil 3          | 0     | 14   |
| 2    | L-Support Rover            | 0     | 15   |
| 2    | EVA Deck 3                 | 0     | 15   |
| 2    | Hangar Bay                 | 0     | 15   |
| 2    | Micro Launch Bay           | 0     | 15   |
| 2    | Water-Fuel Reclamation 1   | 0     | 18   |
| 2    | Fuel Helix Coil 4          | 0     | 18   |
| 2    | Orbital Fuel Scoop 2       | 0     | 20   |
| 2    | EVA Deck 4                 | 0     | 20   |
| 2    | Reactive Hangar Bay        | 0     | 20   |
| 2    | Fuel Helix Coil 5          | 0     | 22   |
| 2    | Orbital Fuel Scoop 3       | 0     | 25   |
| 2    | Orbital Fuel Scoop 4       | 0     | 30   |
| 2    | Water-Fuel Reclamation 2   | 0     | 32   |
| 2    | Fuel Tank 1                | 0     | 40   |
| 2    | Water-Fuel Reclamation 3   | 0     | 40   |
| 2    | Orbital Fuel Scoop 5       | 0     | 40   |
| 2    | Fuel Tank 2                | 0     | 48   |
| 2    | Water-Fuel Reclamation 4   | 0     | 48   |
| 2    | Fuel Tank 3                | 0     | 56   |
| 2    | Water-Fuel Reclamation 5   | 0     | 56   |
| 2    | Reinforced Fuel Tank       | 0     | 64   |
| 2    | Water-Fuel Reclamation 6   | 0     | 64   |
| 2    | Fuel Tank 4                | 0     | 84   |
| 2    | Extraction Drill           | 10    | 0    |
| 2    | Armored Storage            | 10    | 0    |
| 2    | Harvester Bay              | 15    | 10   |
| 2    | Cargo-Fuel Storage         | 15    | 15   |
| 2    | Resource Processor         | 20    | 15   |
| 2    | Storage Hold               | 25    | 0    |
||
| 3    | Battle Launch Bay          | 0     | 20   |
| 3    | Exo-Crawler                | 0     | 25   |
| 3    | Shielded Launch Bay        | 0     | 30   |
| 3    | Reinforced Launch Bay      | 0     | 30   |
| 3    | Launch Bay                 | 0     | 45   |
| 3    | Warhawk Launch Bay         | 0     | 50   |
| 3    | Advanced Launch Bay        | 0     | 60   |
| 3    | Large Fuel Tank 1          | 0     | 75   |
| 3    | Large Fuel Tank 2          | 0     | 95   |
| 3    | Hyperion Launch Bay        | 0     | 100  |
| 3    | Large Fuel Tank 3          | 0     | 135  |
| 3    | Large Fuel Tank 4          | 0     | 160  |
| 3    | Salvage Bay 1              | 10    | 5    |
| 3    | Salvage Bay 2              | 15    | 10   |
| 3    | Armored Salvage Bay 5      | 15    | 15   |
| 3    | Salvage Bay 3              | 20    | 15   |
| 3    | Javat Mechi-Reaper         | 25    | 20   |
| 3    | Salvage Bay 4              | 25    | 20   |
| 3    | Capital Freighter Bridge 5 | 25    | 25   |
| 3    | Cargo Hold 1               | 25    | 40   |
| 3    | Salvage Bay 5              | 30    | 25   |
| 3    | Cargo Hold 2               | 35    | 50   |
| 3    | Fuel-Cargo Hold 4          | 35    | 95   |
| 3    | Fuel-Cargo Hold 5          | 35    | 120  |
| 3    | Salvage Bay 6              | 40    | 40   |
| 3    | Cargo Hold 3               | 40    | 60   |
| 3    | Armored Cargo Hold 4       | 40    | 65   |
| 3    | Cargo Hold 4               | 45    | 70   |
| 3    | Cargo Hold 5               | 50    | 75   |
| 3    | Armored Cargo Hold 5       | 50    | 75   |
| 3    | Cargo Hold 6               | 60    | 75   |
| 3    | Armored Cargo Hold 6       | 60    | 75   |
| 3    | Hauler Hold                | 65    | 40   |
| 3    | Cargo Hold 7               | 70    | 75   |
| 3    | Cargo Hold 8               | 80    | 80   |


### Weapons

Dual-Linked Autocannon, Vanguard Autocannon, Lionheart Cannon, and M95 Tracer Cannon provide bonuses against small craft.

```sqlite3
select
  weapontype as type,
  componentsize as s, componentname as name, skshipops as ops, skgunnery as gun, skelectronics as ele, mass, factionid as faction,
  damage as dmg, damagedice as dice, winties as ties, basetohitcraft as thc, range as rng, ap, accuracy as acc, priority as prio, critchance as crit, effectchance as eff, raddamage as rad, voiddamage as void
from shipcomponent
inner join shipweapon on shipcomponent.shipweaponid = shipweapon._id
where componenttype = 4 and factionid < 10 order by type, s, componentlevel;
```

| type | s |            name            | ops | gun | ele | mass | faction | dmg | dice | ties | thc | rng | ap | acc | prio | crit | eff | rad | void |
|------|---|----------------------------|-----|-----|-----|------|---------|-----|------|------|-----|-----|----|-----|------|------|-----|-----|------|
| 1    | 1 | Valiant Autocannon         | 1   | 4   | 0   | 100  | 0       | 65  | 50   | 1    | 70  | 1   | 1  | 1   | 1    | 5    | 30  | 0   | 0    |
| 1    | 1 | M92 Barrel-Cannon          | 2   | 5   | 0   | 100  | 0       | 75  | 50   | 1    | 70  | 1   | 1  | 3   | 1    | 15   | 40  | 0   | 0    |
| 1    | 1 | Dual-Linked Autocannon     | 2   | 6   | 0   | 100  | 0       | 85  | 50   | 1    | 72  | 1   | 1  | 6   | 1    | 20   | 30  | 0   | 0    |
| 1    | 1 | Vanguard Autocannon        | 3   | 9   | 0   | 100  | 0       | 100 | 50   | 1    | 74  | 1   | 1  | 6   | 1    | 15   | 25  | 0   | 0    |
| 1    | 1 | Lionheart Cannon           | 3   | 10  | 0   | 100  | 0       | 90  | 50   | 1    | 75  | 1   | 1  | 10  | 1    | 15   | 40  | 0   | 0    |
| 1    | 1 | M95 Tracer Cannon          | 3   | 12  | 0   | 100  | 0       | 90  | 60   | 1    | 90  | 1   | 1  | 11  | 1    | 20   | 45  | 0   | 0    |
| 1    | 1 | M101 Tracker Cannon        | 3   | 11  | 0   | 100  | 0       | 95  | 65   | 1    | 75  | 1   | 1  | 12  | 1    | 15   | 40  | 0   | 0    |
| 1    | 2 | M90 Barrel-Cannon          | 2   | 6   | 0   | 300  | 0       | 135 | 52   | 1    | 85  | 1   | 2  | 2   | 1    | 12   | 45  | 0   | 0    |
| 1    | 2 | M94 Barrel-Cannon          | 2   | 7   | 0   | 300  | 0       | 160 | 50   | 1    | 85  | 1   | 2  | 5   | 1    | 10   | 55  | 0   | 0    |
||
| 2    | 1 | Phoenix Lance              | 2   | 4   | 0   | 150  | 0       | 100 | 40   | 0    | 20  | 2   | 2  | 2   | 1    | 15   | 55  | 20  | 0    |
| 2    | 1 | HX-Cycle Lance             | 2   | 5   | 1   | 150  | 0       | 120 | 40   | 0    | 20  | 2   | 2  | 4   | 1    | 15   | 60  | 25  | 0    |
| 2    | 1 | HX-2 Lance                 | 2   | 7   | 1   | 150  | 0       | 140 | 40   | 0    | 20  | 2   | 2  | 6   | 1    | 10   | 55  | 35  | 0    |
| 2    | 1 | Cloudstrike Lance          | 3   | 9   | 1   | 150  | 0       | 180 | 40   | 0    | 20  | 2   | 2  | 6   | 1    | 30   | 30  | 20  | 0    |
| 2    | 1 | Void-Thunder Lance         | 3   | 12  | 2   | 150  | 0       | 180 | 40   | 0    | 25  | 2   | 2  | 9   | 1    | 35   | 30  | 40  | 0    |
| 2    | 2 | Starshot Lance Array       | 2   | 5   | 0   | 350  | 0       | 180 | 40   | 1    | 30  | 2   | 3  | 3   | 1    | 30   | 55  | 30  | 0    |
| 2    | 2 | Starfall Lance Array       | 2   | 9   | 1   | 350  | 0       | 240 | 40   | 0    | 30  | 2   | 3  | 8   | 1    | 15   | 55  | 10  | 0    |
| 2    | 2 | Thunder XK3 Lance Array    | 3   | 10  | 2   | 350  | 0       | 275 | 40   | 0    | 30  | 2   | 3  | 8   | 1    | 10   | 55  | 10  | 0    |
| 2    | 2 | Hazuk Duo-Arc              | 4   | 13  | 3   | 350  | 6       | 280 | 40   | 0    | 15  | 2   | 3  | 10  | 1    | 10   | 60  | 45  | 0    |
| 2    | 2 | Cerulean Tri-Arc           | 4   | 13  | 3   | 350  | 2       | 310 | 40   | 0    | 50  | 2   | 3  | 11  | 1    | 20   | 65  | 35  | 0    |
||
| 3    | 1 | Imperator PC-1             | 1   | 4   | 0   | 100  | 0       | 116 | 20   | 0    | 10  | 3   | 2  | 1   | 2    | 15   | 40  | 22  | 0    |
| 3    | 1 | Stalwart PC-1              | 2   | 5   | 1   | 100  | 0       | 120 | 20   | 0    | 10  | 3   | 2  | 2   | 2    | 30   | 40  | 30  | 0    |
| 3    | 1 | Commander PC-1             | 2   | 7   | 1   | 100  | 0       | 100 | 20   | 0    | 10  | 3   | 2  | 4   | 2    | 25   | 40  | 80  | 0    |
| 3    | 1 | X2 Plasma Battery          | 3   | 9   | 2   | 100  | 0       | 120 | 20   | 0    | 10  | 3   | 2  | 6   | 2    | 30   | 30  | 90  | 0    |
| 3    | 2 | Imperator Plasma Artillery | 2   | 6   | 1   | 300  | 0       | 140 | 20   | 0    | 5   | 3   | 3  | 6   | 2    | 25   | 40  | 90  | 0    |
| 3    | 2 | MK Plasma Ordnance         | 2   | 9   | 1   | 300  | 0       | 150 | 20   | 0    | 5   | 3   | 3  | 5   | 2    | 25   | 40  | 110 | 0    |
| 3    | 2 | Commander Plasma Artillery | 3   | 11  | 2   | 300  | 0       | 150 | 20   | 0    | 5   | 3   | 3  | 10  | 2    | 30   | 30  | 130 | 0    |
| 3    | 2 | Azmath Plasma Ordnance     | 3   | 12  | 2   | 300  | 0       | 150 | 20   | 0    | 5   | 3   | 3  | 11  | 2    | 30   | 40  | 160 | 0    |
| 3    | 3 | Obliterator PK-1           | 2   | 9   | 2   | 550  | 0       | 150 | 20   | 0    | 5   | 3   | 4  | 7   | 2    | 30   | 45  | 150 | 0    |
| 3    | 3 | Interceder PCX-1           | 2   | 9   | 2   | 550  | 0       | 50  | 30   | 0    | 5   | 3   | 4  | 8   | 2    | 35   | 50  | 200 | 0    |
| 3    | 3 | Obliterator PK-2           | 3   | 11  | 2   | 550  | 0       | 150 | 20   | 0    | 5   | 3   | 4  | 9   | 2    | 35   | 45  | 170 | 0    |
| 3    | 3 | Obliterator PKX-3          | 4   | 11  | 2   | 550  | 0       | 150 | 20   | 0    | 5   | 3   | 4  | 11  | 2    | 35   | 50  | 190 | 0    |
| 3    | 3 | Interceder PCX-5           | 3   | 12  | 3   | 550  | 0       | 50  | 30   | 0    | 5   | 3   | 4  | 10  | 2    | 35   | 50  | 275 | 0    |
||
| 4    | 1 | Light Railgun              | 2   | 3   | 0   | 125  | 0       | 90  | 20   | 0    | 60  | 3   | 3  | 3   | 1    | 5    | 35  | 0   | 80   |
| 4    | 1 | Lightspear Railgun         | 2   | 4   | 2   | 125  | 0       | 100 | 20   | 0    | 60  | 3   | 3  | 5   | 1    | 10   | 35  | 0   | 90   |
| 4    | 1 | Blazelight Railgun         | 2   | 6   | 2   | 125  | 0       | 100 | 20   | 0    | 60  | 3   | 3  | 7   | 1    | 10   | 40  | 0   | 100  |
| 4    | 1 | Radiance Railgun           | 3   | 8   | 3   | 125  | 0       | 80  | 20   | 0    | 60  | 3   | 3  | 8   | 1    | 10   | 60  | 0   | 110  |
| 4    | 2 | Archangel Railgun          | 2   | 5   | 0   | 300  | 0       | 120 | 20   | 1    | 65  | 3   | 3  | 4   | 1    | 10   | 45  | 0   | 84   |
| 4    | 2 | Helios Railgun             | 3   | 6   | 1   | 300  | 0       | 120 | 20   | 0    | 65  | 3   | 3  | 6   | 1    | 20   | 45  | 0   | 90   |
| 4    | 2 | Helios X Railgun           | 3   | 6   | 1   | 310  | 0       | 122 | 20   | 0    | 65  | 3   | 3  | 7   | 1    | 25   | 55  | 0   | 100  |
| 4    | 2 | Archangel Dual-R Railgun   | 3   | 6   | 1   | 300  | 0       | 125 | 20   | 0    | 65  | 3   | 3  | 10  | 1    | 20   | 45  | 0   | 110  |
| 4    | 2 | Elomag Railgun             | 4   | 9   | 2   | 300  | 0       | 130 | 20   | 0    | 65  | 3   | 3  | 10  | 1    | 20   | 45  | 0   | 120  |
| 4    | 2 | Helios X2 Railgun Array    | 4   | 9   | 2   | 300  | 0       | 200 | 20   | 0    | 65  | 3   | 4  | 12  | 1    | 20   | 45  | 0   | 140  |
| 4    | 2 | Tri Helical Rail X3        | 4   | 10  | 2   | 300  | 0       | 200 | 20   | 0    | 65  | 3   | 4  | 14  | 1    | 25   | 45  | 0   | 190  |
| 4    | 2 | Demon-X Heavy Rail         | 5   | 11  | 2   | 300  | 0       | 240 | 40   | 0    | 60  | 3   | 4  | 15  | 1    | 20   | 55  | 0   | 200  |
| 4    | 2 | Demon-X Fast Rail          | 4   | 10  | 2   | 300  | 0       | 200 | 30   | 0    | 50  | 3   | 3  | 11  | 1    | 25   | 40  | 0   | 200  |
||
| 5    | 2 | Vengence Gravcannon        | 1   | 5   | 0   | 325  | 0       | 180 | 90   | 1    | 0   | 2   | 3  | 0   | 2    | 15   | 30  | 0   | 0    |
| 5    | 2 | Retaliation Gravcannon     | 2   | 5   | 0   | 350  | 0       | 185 | 90   | 1    | 0   | 2   | 3  | 2   | 2    | 30   | 40  | 0   | 0    |
| 5    | 2 | JUK Gravity Array          | 2   | 6   | 0   | 350  | 0       | 200 | 90   | 1    | 0   | 2   | 3  | 2   | 2    | 35   | 40  | 0   | 0    |
| 5    | 2 | JUK Gravcannon             | 2   | 8   | 0   | 350  | 0       | 215 | 90   | 1    | 0   | 2   | 3  | 3   | 2    | 35   | 40  | 0   | 0    |
| 5    | 2 | JUK-22 Gravcannon          | 2   | 9   | 0   | 350  | 0       | 240 | 90   | 1    | 0   | 2   | 3  | 3   | 2    | 30   | 40  | 0   | 0    |
| 5    | 2 | JUK-24 Gravcannon          | 3   | 10  | 0   | 350  | 0       | 250 | 90   | 1    | 0   | 2   | 3  | 4   | 2    | 30   | 40  | 0   | 0    |
| 5    | 3 | Ruut 82 Gravcannon         | 2   | 8   | 0   | 600  | 0       | 300 | 100  | 1    | 0   | 2   | 4  | 3   | 2    | 40   | 40  | 0   | 0    |
| 5    | 3 | Ruut 84 Gravcannon         | 2   | 12  | 0   | 600  | 0       | 320 | 100  | 1    | 0   | 2   | 4  | 4   | 2    | 45   | 40  | 0   | 0    |
| 5    | 3 | Retribution Gravcannon     | 3   | 13  | 0   | 600  | 0       | 350 | 100  | 1    | 0   | 2   | 4  | 5   | 2    | 45   | 40  | 0   | 0    |
| 5    | 3 | Coronation Gravcannon      | 2   | 15  | 0   | 600  | 0       | 400 | 100  | 1    | 0   | 2   | 4  | 6   | 2    | 20   | 65  | 0   | 0    |
||
| 6    | 1 | Hydra Missile Array        | 2   | 4   | 1   | 125  | 0       | 120 | 100  | 0    | 30  | 4   | 3  | 8   | 2    | 30   | 30  | 25  | 0    |
| 6    | 1 | Arratech Missile Pod       | 2   | 6   | 1   | 125  | 0       | 125 | 100  | 0    | 30  | 4   | 3  | 10  | 2    | 30   | 25  | 30  | 0    |
| 6    | 1 | Aramech Missile Pod        | 2   | 8   | 1   | 125  | 0       | 130 | 100  | 0    | 30  | 4   | 3  | 11  | 2    | 25   | 30  | 35  | 0    |
| 6    | 1 | Dracos Missile Array       | 2   | 9   | 1   | 125  | 0       | 140 | 100  | 0    | 30  | 4   | 3  | 13  | 2    | 25   | 25  | 40  | 0    |
| 6    | 1 | Dracos X2 Missile Battery  | 2   | 11  | 1   | 125  | 0       | 140 | 100  | 0    | 30  | 4   | 3  | 15  | 2    | 30   | 25  | 45  | 0    |
| 6    | 1 | Aramech X2 Missile Battery | 2   | 12  | 1   | 125  | 0       | 130 | 100  | 0    | 30  | 4   | 3  | 17  | 2    | 35   | 30  | 50  | 0    |
| 6    | 1 | Valkri Missile Pods        | 2   | 13  | 2   | 125  | 0       | 130 | 100  | 0    | 30  | 4   | 3  | 18  | 2    | 30   | 30  | 90  | 0    |
| 6    | 1 | Gargoyle Missile Battery   | 2   | 12  | 1   | 125  | 0       | 150 | 100  | 0    | 35  | 4   | 3  | 17  | 2    | 15   | 40  | 50  | 0    |
| 6    | 2 | Ares Missile System        | 1   | 4   | 1   | 300  | 0       | 110 | 100  | 0    | 40  | 4   | 3  | 6   | 2    | 30   | 25  | 20  | 0    |
| 6    | 2 | Vector Missile System      | 3   | 7   | 1   | 300  | 0       | 140 | 100  | 0    | 40  | 4   | 3  | 8   | 2    | 30   | 15  | 30  | 0    |
| 6    | 2 | Dual-Linked Vector Missile | 3   | 10  | 1   | 300  | 0       | 160 | 100  | 0    | 40  | 4   | 3  | 10  | 2    | 30   | 20  | 60  | 0    |
| 6    | 2 | Goliath Missile Battery    | 3   | 12  | 2   | 300  | 0       | 170 | 100  | 0    | 40  | 4   | 3  | 14  | 2    | 40   | 25  | 80  | 0    |
||
| 7    | 1 | Hellfire Torpedo           | 2   | 4   | 0   | 110  | 0       | 20  | 40   | 0    | 20  | 5   | 2  | 4   | 1    | 2    | 45  | 0   | 30   |
| 7    | 1 | Firestorm Torpedo          | 2   | 6   | 1   | 110  | 0       | 30  | 40   | 0    | 20  | 5   | 2  | 8   | 1    | 3    | 50  | 0   | 40   |
| 7    | 1 | Inferno Torpedo            | 2   | 11  | 2   | 110  | 0       | 35  | 40   | 0    | 20  | 5   | 2  | 10  | 1    | 8    | 50  | 0   | 45   |
| 7    | 1 | Torpedo Dual-Laced Array   | 3   | 13  | 3   | 110  | 0       | 35  | 55   | 0    | 20  | 5   | 2  | 14  | 1    | 8    | 50  | 0   | 45   |
| 7    | 1 | Firewave Torpedo           | 2   | 15  | 4   | 110  | 0       | 40  | 60   | 0    | 25  | 5   | 2  | 16  | 1    | 10   | 60  | 0   | 70   |
| 7    | 2 | Torpedo Mk-Alpha           | 1   | 5   | 1   | 325  | 0       | 30  | 40   | 0    | 10  | 5   | 2  | 5   | 1    | 2    | 45  | 0   | 40   |
| 7    | 2 | Void-Lance Torpedo         | 3   | 7   | 3   | 325  | 0       | 30  | 70   | 0    | 10  | 5   | 3  | 11  | 1    | 5    | 65  | 0   | 80   |
| 7    | 2 | Torpedo MK2-Alpha          | 3   | 13  | 3   | 325  | 0       | 40  | 50   | 0    | 10  | 5   | 3  | 14  | 1    | 10   | 60  | 0   | 90   |
| 7    | 3 | Cadonya Buster Array       | 6   | 16  | 6   | 600  | 2       | 100 | 60   | 0    | 50  | 5   | 4  | 16  | 1    | 12   | 65  | 0   | 80   |


### TODO


### Mass Redux

```sqlite3
select componentsize as size, componentname as name, skPilot as pil, skShipOps as ops, skElectronics as elec, skNavigation as nav, factionid as faction, jumpcost as jmp, mass, abs(mass)/jumpcost as value from shipcomponent where componenttype = 27 and factionid < 10 order by size, mass desc;
```

| size |         name         | pil | ops | elec | nav | faction | jmp | mass | value |
|------|----------------------|-----|-----|------|-----|---------|-----|------|-------|
| 1    | Mass Modulator 1     | 2   | 0   | 0    | 0   | 0       | 1   | -100 | 100   |
| 1    | Mass Modulator 2     | 2   | 0   | 1    | 0   | 0       | 2   | -125 | 62    |
| 1    | Mass Dampener 1      | 0   | 1   | 0    | 0   | 0       | 2   | -150 | 75    |
| 1    | Mass Modulator 3     | 3   | 0   | 1    | 0   | 0       | 3   | -150 | 50    |
| 1    | Mass Modulator 4     | 3   | 0   | 2    | 0   | 0       | 5   | -165 | 33    |
| 1    | Mass Dampener 2      | 0   | 2   | 0    | 1   | 0       | 4   | -180 | 45    |
| 1    | Mass Dampener 3      | 0   | 3   | 0    | 2   | 0       | 5   | -210 | 42    |
| 1    | Mass Dampener 4      | 0   | 3   | 0    | 2   | 0       | 6   | -240 | 40    |
||
| 2    | Mass Reducer 1       | 0   | 1   | 1    | 0   | 0       | 2   | -225 | 112   |
| 2    | Mass Reducer 2       | 0   | 2   | 2    | 0   | 0       | 3   | -240 | 80    |
| 2    | Mass Reducer 3       | 0   | 2   | 3    | 0   | 0       | 4   | -260 | 65    |
| 2    | Mass Reducer 4       | 0   | 2   | 4    | 0   | 0       | 5   | -280 | 56    |
| 2    | Adv. Mass Dampener 1 | 0   | 2   | 0    | 1   | 0       | 5   | -300 | 60    |
| 2    | Hawk Mass Reducer 4  | 5   | 1   | 0    | 0   | 8       | 4   | -300 | 75    |
| 2    | Lion Mass Reducer 4  | 0   | 1   | 5    | 0   | 4       | 4   | -300 | 75    |
| 2    | Adv. Mass Dampener 2 | 0   | 3   | 0    | 1   | 0       | 7   | -330 | 47    |
| 2    | Adv. Mass Dampener 3 | 0   | 4   | 0    | 2   | 0       | 8   | -360 | 45    |
| 2    | Adv. Mass Dampener 4 | 0   | 5   | 0    | 3   | 0       | 9   | -400 | 44    |
| 2    | Adv. Mass Dampener 5 | 0   | 5   | 0    | 3   | 0       | 12  | -460 | 38    |


## Ships

Starting Ships:

```sqlite3
select shiptypename, unlockid > 0 as lock from shiptype where startingship = 1 order by basemass;
```

|     shipTypeName     | lock | prio |
|----------------------|------|------|
| Juror Class          | 0    | E    |
| Scout Cutter         | 0    | D    |
| Reach Vindex         | 1    | D    |
| Longbolt             | 1    | D    |
| Paladin Cruiser      | 0    | C    |
| Frontier Liner       | 0    | C    |
| Galtak Freighter     | 1    | C    |
| Aeternum Vindex      | 1    | B    |
| Palace Interceptor   | 1    | B    |
| Fidelis Cutter       | 0    | B    |
| Guardian Interceptor | 0    | B    |
| Stellar Falcon       | 0    | A    |
| Cautela Heavylift    | 0    | A    |
| Dragoon Cruiser      | 0    | A    |
| Degla Megalift       | 1    | A    |
| Shizari Huntress     | 1    | A    |


```sqlite3
select basemass as mass, unlockid > 0 as lock, shiptypename as name, hullpoints as hull, basearmor as arm, basedeflection as shld, basefuel as fuel, maxofficer as off, maxlifesupport as crew, smallslots as s, mediumslots as m, largeslots as l, _id in (select shipId from shipdatacompartment where componenttype = 1 and size = 1) as scout, factionid as f from shiptype where startingship > 0 order by mass, off, crew;
```

| mass | lock |           name            | hull | arm | shld | fuel | off | crew | s  | m  | l | scout | f |
|------|------|---------------------------|------|-----|------|------|-----|------|----|----|---|-------|---|
| 2400 | 0    | Scout Cutter              | 900  | 12  | 12   | 60   | 4   | 24   | 11 | 3  | 2 | 0     | 0 |
| 2400 | 0    | Allistar Liner            | 1000 | 10  | 14   | 95   | 4   | 24   | 10 | 3  | 2 | 1     | 0 |
| 2400 | 1    | Reach Vindex              | 1000 | 10  | 14   | 95   | 4   | 24   | 11 | 3  | 2 | 1     | 0 |
| 2400 | 0    | Volk Frigate              | 1350 | 6   | 12   | 45   | 5   | 24   | 11 | 3  | 2 | 1     | 0 |
| 2400 | 1    | Aeternum Vindex           | 1000 | 14  | 10   | 70   | 5   | 24   | 10 | 4  | 2 | 1     | 0 |
| 2400 | 0    | Zartar Fang               | 1250 | 8   | 8    | 50   | 5   | 24   | 9  | 6  | 2 | 1     | 6 |
| 2400 | 0    | Gunhawk Sabre             | 1100 | 12  | 12   | 60   | 6   | 18   | 10 | 7  | 1 | 1     | 3 |
| 2400 | 0    | Caliga Vindex             | 1275 | 14  | 10   | 95   | 6   | 24   | 14 | 3  | 2 | 1     | 6 |
||
| 3400 | 0    | Juror Class               | 1100 | 10  | 10   | 55   | 4   | 24   | 9  | 4  | 2 | 0     | 0 |
| 3400 | 0    | Lightbow Raptor           | 1200 | 12  | 10   | 25   | 4   | 24   | 9  | 5  | 2 | 0     | 0 |
| 3400 | 0    | Strikecruiser             | 1250 | 12  | 10   | 75   | 4   | 24   | 10 | 4  | 3 | 0     | 0 |
| 3400 | 0    | Vulture Liner             | 1000 | 8   | 12   | 85   | 4   | 24   | 10 | 4  | 2 | 1     | 0 |
| 3400 | 1    | Longbolt                  | 1000 | 8   | 12   | 60   | 4   | 24   | 11 | 4  | 2 | 0     | 0 |
| 3400 | 0    | Bolt Raptor               | 1050 | 11  | 12   | 80   | 5   | 24   | 12 | 4  | 2 | 1     | 0 |
| 3400 | 0    | Dart Liner                | 950  | 10  | 15   | 45   | 5   | 24   | 12 | 3  | 2 | 1     | 0 |
| 3400 | 1    | Palace Interceptor        | 1200 | 11  | 11   | 70   | 5   | 24   | 8  | 6  | 2 | 1     | 0 |
| 3400 | 0    | Corsair Interceptor       | 1250 | 10  | 10   | 55   | 5   | 24   | 13 | 3  | 2 | 1     | 1 |
| 3400 | 0    | Dart Jammer               | 1000 | 15  | 8    | 45   | 5   | 30   | 11 | 4  | 2 | 0     | 0 |
| 3400 | 0    | Callus Freighter          | 1500 | 5   | 12   | 50   | 5   | 30   | 11 | 4  | 3 | 0     | 0 |
| 3400 | 1    | Victus Interceptor        | 1100 | 12  | 10   | 64   | 5   | 30   | 11 | 4  | 3 | 1     | 0 |
| 3400 | 0    | Sword Cutter              | 1900 | 7   | 8    | 70   | 5   | 30   | 11 | 6  | 2 | 1     | 2 |
| 3400 | 0    | Wolf Vector               | 1700 | 10  | 6    | 100  | 5   | 30   | 11 | 6  | 2 | 1     | 0 |
| 3400 | 0    | Rim Exocruiser            | 1100 | 12  | 10   | 105  | 5   | 30   | 11 | 5  | 2 | 1     | 5 |
||
| 5000 | 0    | Paladin Cruiser           | 1500 | 8   | 7    | 40   | 5   | 30   | 10 | 5  | 4 | 0     | 0 |
| 5000 | 0    | Frontier Liner            | 1400 | 7   | 8    | 55   | 5   | 30   | 10 | 5  | 3 | 0     | 0 |
| 5000 | 1    | Galtak Freighter          | 1600 | 8   | 5    | 30   | 5   | 30   | 12 | 3  | 4 | 0     | 0 |
| 5000 | 0    | Longbow Cruiser           | 1500 | 9   | 8    | 25   | 5   | 30   | 11 | 6  | 4 | 0     | 0 |
| 5000 | 0    | Solar Predator            | 1950 | 7   | 9    | 80   | 5   | 30   | 11 | 5  | 4 | 0     | 0 |
| 5000 | 0    | Hammerhead Jammer         | 2000 | 8   | 5    | 50   | 5   | 30   | 10 | 5  | 4 | 0     | 0 |
| 5000 | 0    | Paladin Defender          | 1500 | 12  | 6    | 30   | 5   | 30   | 10 | 5  | 4 | 0     | 0 |
| 5000 | 0    | Vrax Hauler               | 1000 | 12  | 9    | 100  | 5   | 30   | 10 | 7  | 4 | 0     | 0 |
| 5000 | 0    | Paladin Cutter            | 1600 | 7   | 11   | 40   | 5   | 30   | 12 | 5  | 4 | 0     | 0 |
| 5000 | 0    | Galtak Heavylift          | 1500 | 7   | 7    | 50   | 5   | 30   | 11 | 5  | 5 | 0     | 0 |
| 5000 | 0    | Royale Gladius            | 1100 | 10  | 10   | 55   | 5   | 30   | 12 | 5  | 4 | 0     | 4 |
| 5000 | 0    | Strikecarrier             | 1350 | 8   | 12   | 60   | 5   | 30   | 12 | 5  | 4 | 0     | 0 |
| 5000 | 0    | Reach Carrier             | 1500 | 10  | 10   | 55   | 5   | 30   | 10 | 7  | 4 | 0     | 0 |
| 5000 | 0    | Reach Cruiser             | 1650 | 12  | 8    | 75   | 5   | 30   | 11 | 6  | 4 | 0     | 8 |
| 5000 | 0    | Reach Defender            | 1750 | 11  | 10   | 45   | 5   | 30   | 10 | 7  | 4 | 0     | 2 |
| 5000 | 0    | Arcanum Freighter         | 1600 | 9   | 8    | 50   | 5   | 30   | 12 | 5  | 4 | 0     | 9 |
||
| 6000 | 0    | Fidelis Cutter            | 2000 | 7   | 8    | 60   | 5   | 30   | 12 | 7  | 4 | 0     | 0 |
| 6000 | 0    | Guardian Interceptor      | 1950 | 6   | 6    | 60   | 5   | 30   | 12 | 7  | 4 | 0     | 0 |
| 6000 | 0    | Stellar Falcon            | 2050 | 5   | 9    | 75   | 5   | 30   | 13 | 6  | 4 | 0     | 0 |
| 6000 | 1    | Horizon Highliner         | 2495 | 4   | 9    | 40   | 6   | 30   | 10 | 8  | 5 | 0     | 0 |
| 6000 | 0    | Raptor Class              | 1600 | 2   | 10   | 80   | 6   | 36   | 11 | 8  | 4 | 0     | 0 |
| 6000 | 0    | Vengeance Class           | 2350 | 8   | 3    | 45   | 6   | 36   | 13 | 6  | 5 | 0     | 0 |
| 6000 | 0    | Crimson Defender          | 1900 | 9   | 5    | 65   | 6   | 36   | 12 | 7  | 4 | 0     | 3 |
| 6000 | 0    | Azure Defender            | 1850 | 4   | 9    | 130  | 7   | 36   | 12 | 7  | 4 | 0     | 7 |
| 6000 | 0    | Lockwood Defender         | 2005 | 10  | 10   | 55   | 7   | 36   | 10 | 8  | 5 | 0     | 3 |
| 6000 | 1    | Horizon  Cruiser          | 2250 | 5   | 10   | 60   | 7   | 36   | 9  | 9  | 5 | 0     | 0 |
| 6000 | 0    | Neutiquam Cruiser         | 2050 | 10  | 10   | 150  | 7   | 36   | 12 | 9  | 5 | 0     | 6 |
| 6000 | 0    | Fallen Carrier            | 1850 | 4   | 7    | 130  | 7   | 36   | 8  | 9  | 5 | 0     | 0 |
| 6000 | 0    | Extremis Carrier          | 2005 | 5   | 8    | 80   | 7   | 36   | 7  | 10 | 5 | 0     | 0 |
| 6000 | 0    | Vark Carrier              | 2500 | 9   | 10   | 90   | 7   | 36   | 8  | 10 | 5 | 0     | 9 |
| 6000 | 1    | Shizari Huntress          | 2050 | 7   | 8    | 100  | 7   | 36   | 14 | 7  | 4 | 1     | 0 |
||
| 7000 | 0    | Cautela Heavylift         | 2500 | 5   | 4    | 80   | 6   | 36   | 12 | 8  | 4 | 0     | 0 |
| 7000 | 0    | Dragoon Cruiser           | 2350 | 6   | 5    | 100  | 6   | 36   | 12 | 8  | 4 | 0     | 0 |
| 7000 | 0    | Tiberian Highliner        | 2200 | 6   | 5    | 120  | 6   | 42   | 13 | 7  | 6 | 0     | 5 |
| 7000 | 1    | Degla Megalift            | 1900 | 7   | 9    | 75   | 7   | 36   | 12 | 9  | 5 | 0     | 0 |
| 7000 | 1    | Azurite Cruiser           | 1850 | 9   | 3    | 130  | 7   | 36   | 11 | 10 | 4 | 0     | 2 |
| 7000 | 0    | Basalt Carrier            | 1850 | 4   | 7    | 130  | 7   | 36   | 12 | 8  | 6 | 0     | 0 |
| 7000 | 0    | Leo Battlecruiser         | 2000 | 8   | 7    | 95   | 7   | 42   | 12 | 9  | 6 | 0     | 4 |
| 7000 | 1    | Obsidian Carrier          | 2650 | 2   | 10   | 80   | 7   | 42   | 11 | 8  | 6 | 0     | 0 |
| 7000 | 1    | Larimar Battlecruiser     | 2250 | 4   | 11   | 100  | 7   | 42   | 10 | 10 | 5 | 0     | 2 |
||
| 8000 | 0    | Aegis Freighter           | 2200 | 9   | 7    | 50   | 7   | 36   | 8  | 13 | 7 | 0     | 7 |
| 8000 | 1    | Pallas Freighter          | 2050 | 7   | 11   | 95   | 7   | 36   | 9  | 11 | 8 | 0     | 0 |
| 8000 | 0    | Tempus Freighter          | 2900 | 6   | 10   | 150  | 7   | 36   | 9  | 11 | 8 | 0     | 1 |
| 8000 | 0    | Broadsword Class          | 2600 | 5   | 3    | 60   | 7   | 42   | 13 | 9  | 7 | 0     | 0 |
| 8000 | 0    | Warhammer Class           | 2500 | 3   | 9    | 35   | 7   | 42   | 12 | 11 | 7 | 0     | 0 |
| 8000 | 0    | Mortifor Carrier          | 2350 | 10  | 6    | 60   | 7   | 42   | 15 | 8  | 6 | 0     | 5 |
| 8000 | 0    | Harbinger Carrier         | 2100 | 7   | 11   | 95   | 7   | 42   | 12 | 10 | 6 | 0     | 8 |
| 8000 | 1    | Skylift Carrier           | 1850 | 8   | 10   | 135  | 7   | 42   | 14 | 8  | 6 | 0     | 4 |
||
| 9000 | 0    | Sword Battlecruiser       | 2100 | 9   | 7    | 115  | 7   | 42   | 14 | 12 | 6 | 0     | 0 |
| 9000 | 0    | Cautela Titan             | 2700 | 7   | 4    | 160  | 7   | 42   | 12 | 13 | 6 | 0     | 0 |
| 9000 | 0    | Dreadnought Battlecarrier | 2500 | 8   | 8    | 135  | 7   | 42   | 12 | 12 | 8 | 0     | 1 |
